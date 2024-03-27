from model.user import PublicUser, PrivateUser, SignInUser
from .init import conn, curs, get_db, IntegrityError
from error import Missing, Duplicate

curs.execute(
    """create table if not exists
                user(
                  name text primary key,
                  hash text)"""
)
curs.execute(
    """create table if not exists
                xuser(
                  name text primary key,
                  hash text)"""
)


# is_public 인자에 따라 나가는 모델이 분기된다.
def row_to_model(row: tuple, is_public: bool = True) -> PublicUser | PrivateUser:
    name, hash = row
    if is_public:
        return PublicUser(name=name)
    else:
        return PrivateUser(name=name, hash=hash)


def model_to_dict(user: PrivateUser) -> dict:
    return user.model_dump()


# 유저 조회는 is_public에 따라  PublicUser 또는 PrivateUser를 리턴한다.
def get_one(name: str, is_public: bool = True) -> PublicUser | PrivateUser:
    qry = "select * from user where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row, is_public=is_public)
    else:
        raise Missing(msg=f"User {name} not found")


# 유저리스트 조회에서는 민감정보(hash)를 포함할 일이 없기 때문에 PublicUser 모델 집합을 리턴한다.
def get_all() -> list[PublicUser]:
    qry = "select * from user"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]


# 유저 생성을 위해서는 password를 암호화한 hash 값을 저장해야 한다.
# create 함수는 user 인자가 hash 값을 가지고 있는 것으로 간주한다.
# 저장이 완료되면 외부로 노출되도 되는 PublicUser를 리턴한다.
def create(user: PrivateUser, table: str = "user") -> PublicUser:
    """user 테이블 또는 xuser 테이블에 유저를 생성한다"""
    qry = f"""insert into {table}
        (name, hash)
        values
        (:name, :hash)"""
    params = model_to_dict(user)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(msg=f"{table}: user {user.name} already exists")
    return PublicUser(name=user.name)


# 외부로 노출되는 속성이 name이기 때문에 현재는 name에 대한 변경만 가능하다.
def modify(name: str, user: PublicUser) -> PublicUser:
    """name으로 조회한 유저의 이름을 수정한다"""
    qry = """update user set
             name=:name
             where name=:name0"""
    params = {"name": user.name, "name0": name}
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return get_one(user.name)
    else:
        raise Missing(msg=f"User {name} not found")


def delete(name: str) -> None:
    """name으로 user 테이블에서 조회한 유저를 삭제하고, xuser 테이블에 추가한다"""
    user = get_one(name, is_public=False)
    qry = "delete from user where name = :name"
    params = {"name": name}
    curs.execute(qry, params)
    if curs.rowcount != 1:
        raise Missing(msg=f"User {name} not found")
    create(user, table="xuser")

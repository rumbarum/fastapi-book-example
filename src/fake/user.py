from model.user import SignInUser, PrivateUser, PublicUser
from error import Missing, Duplicate

# 이 모듈에서는 hash 비밀번호 검증을 하지 않는다.
fakes = [
    PublicUser(name="kwijobo"),
    PublicUser(name="ermagerd"),
]


def find(name: str) -> PublicUser | None:
    for e in fakes:
        if e.name == name:
            return e
    return None


def check_missing(name: str):
    if not find(name):
        raise Missing(msg=f"Missing user {name}")


def check_duplicate(name: str):
    if find(name):
        raise Duplicate(msg=f"Duplicate user {name}")


def get_all() -> list[PublicUser]:
    """모든 유저를 반환 한다"""
    return fakes


def get_one(name: str) -> PublicUser:
    """한 유저를 반환 한다"""
    check_missing(name)
    return find(name)


def create(user: PublicUser) -> PublicUser:
    """유저를 생성한다"""
    check_duplicate(user.name)
    return PublicUser(name=user.name)


def modify(name: str, user: PublicUser) -> PublicUser:
    """유저를 수정한다"""
    check_missing(name)
    return user


def delete(name: str) -> None:
    """유저를 삭제한다"""
    check_missing(name)
    return None

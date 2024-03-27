from model.creature import Creature

# 데이터베이스와 SQL로 바꿀 때까지 사용할 가짜 데이터
_creatures = [
    Creature(
        name="Yeti",
        aka="Abominable Snowman",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
    ),
    Creature(
        name="Bigfoot", description="Yeti's Cousin Eddie", country="US", area="*", aka="Sasquatch"
    ),
]


def get_all() -> list[Creature]:
    """생명체 목록을 반환한다."""
    return _creatures


def get_one(name: str) -> Creature | None:
    """검색한 생명체를 반환한다."""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None


# 다음 함수는 현재 올바로 동작하지 않는다.
# 실제로는 _creatures 목록을 수정하지 않지만,
# 마치 작동하는 것처럼 동작한다.
def create(creature: Creature) -> Creature:
    """생명체를 추가한다."""
    return creature


def modify(name: str, creature: Creature) -> Creature:
    """생명체의 정보를 일부 수정한다."""
    return creature


def replace(name: str, creature: Creature) -> Creature:
    """생명체를 완전히 교체한다."""
    return creature


def delete(name: str) -> bool:
    """생명체를 삭제한다. 만약 대상이 없다면 False를 반환한다."""
    for _creature in _creatures:
        if _creature.name == name:
            return True
    return False

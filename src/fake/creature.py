from error import Duplicate, Missing
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


def get_one(name: str) -> Creature:
    """검색한 생명체를 반환한다."""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    raise Missing(msg=f"Creature {name} not found")


def create(creature: Creature) -> Creature:
    """생명체를 추가한다."""
    if next((x for x in _creatures if x.name == creature.name), None):
        raise Duplicate(msg=f"Creature {creature.name} already exists")
    _creatures.append(creature)
    return creature


def modify(name: str, creature: Creature) -> Creature:
    """생명체의 정보를 일부 수정한다."""
    _creature = next((x for x in _creatures if x.name == creature.name), None)
    if _creature is not None:
        _creature = creature
        return _creature
    else:
        raise Missing(msg=f"Creature {name} not found")


def replace(name: str, creature: Creature) -> Creature:
    """생명체를 완전히 교체한다."""
    _creature = next((x for x in _creatures if x.name == creature.name), None)
    if _creature is None:
        raise Missing(msg=f"Creature {name} not found")

    _creature = creature
    return _creature


def delete(name: str) -> bool:
    """생명체를 삭제한다. 만약 대상이 없다면 None을 반환한다."""
    if not name:
        return False

    _creature = next((x for x in _creatures if x.name == name), None)
    if _creature is None:
        raise Missing(msg=f"Explorer {name} not found")

    _creatures.remove(_creature)
    return True

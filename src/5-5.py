from collections import namedtuple

CreatureNamedTuple = namedtuple("CreatureNamedTuple", "name, country, area, description, aka")
namedtuple_thing = CreatureNamedTuple(
    "yeti", "CN", "Himalaya", "Hirsute HImalayan", "Abominable Snowman"
)
print("Name is", namedtuple_thing[0])
print("Name is", namedtuple_thing.name)

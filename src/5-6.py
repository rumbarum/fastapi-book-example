class CreatureClass:
    def __init__(self, name: str, country: str, area: str, description: str, aka: str):
        self.name = name
        self.country = country
        self.area = area
        self.description = description
        self.aka = aka


class_thing = CreatureClass("yeti", "CN", "Himalayas", "Hirsute Himalayan", "Abominable Snowman")

print("Name is", class_thing.name)

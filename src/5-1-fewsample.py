# 5-1
physics_magic_number: float = 1.0 / 137.03599913
hp_lovecraft_noun: str = "ichor"
exploding_sheep: tuple = "sis", "boom", "bah!"
responses: dict = {"Marco": "Polo", "answer": 42}

# 5-2
from typing import Any

responses: dict[str, Any] = {"Marco": "Polo", "answer": 42}

from typing import Union

responses: dict[str, Union[str, int]] = {"Marco": "Polo", "answer": 42}

# 3.10 이상 동작
responses: dict[str, str | int] = {"Marco": "Polo", "answer": 42}

# thing0
thing0: str


thing1: str = "yeti"
thing1 = 47


def get_thing() -> str:
    return "yeti"

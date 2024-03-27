import os

if os.getenv("UNIT_TEST"):
    import fake_mod1 as mod1
else:
    import mod1


def summer(x: int, y: int) -> str:
    return mod1.preamble() + f"{x+y}"

import data.game as data


def get_word() -> str:
    return data.get_word()


from collections import Counter, defaultdict

HIT = "H"
MISS = "M"
CLOSE = "C"  # (문자가 맞지만 위치가 틀렸다.)
ERROR = ""


def get_score(actual: str, guess: str) -> str:
    length: int = len(actual)
    if len(guess) != length:
        return ERROR
    actual_counter = Counter(actual)  #  {letter: count, ...}
    guess_counter = defaultdict(int)
    result = [MISS] * length
    for pos, letter in enumerate(guess):
        if letter == actual[pos]:
            result[pos] = HIT
            guess_counter[letter] += 1
    for pos, letter in enumerate(guess):
        if result[pos] == HIT:
            continue
        guess_counter[letter] += 1
        if letter in actual and guess_counter[letter] <= actual_counter[letter]:
            result[pos] = CLOSE
    result = "".join(result)
    return result

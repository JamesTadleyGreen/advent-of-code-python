import random
from typing import Callable

from timer import timer


def compare(
    code: dict[str, tuple[Callable, Callable]], input: str, anonomise: bool = True
):
    keys = list(code.keys())
    if anonomise:
        random.shuffle(keys)
    for k in keys:
        if not anonomise:
            print(k)
        first = timer(code[k][0], input)
        second = timer(code[k][1], input)
        print(f"Total time: {(first+second)*1_000:.1f}ms")

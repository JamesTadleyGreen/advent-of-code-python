from timeit import Timer
from typing import Callable


def timer(func: Callable[[str], int], input: str, number_of_runs: int | None = None):
    result = func(input)
    print(f"{func.__name__}: {result}", end="")
    timer = Timer("func(input)", globals=locals())
    if number_of_runs is None:
        number_of_runs, total_time = timer.autorange()
    else:
        total_time = timer.timeit(number_of_runs)
    print(f" ({total_time*1_000/number_of_runs:.3f}ms) ({number_of_runs} runs)")
    return total_time / number_of_runs

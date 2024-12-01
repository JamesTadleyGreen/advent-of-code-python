import argparse
import timeit
from typing import Callable
import os

from importer import import_module_from_path
from input import download_input


def get_latest_year() -> int:
    return max([folder.split('-')[1] for folder in os.listdir('aoc')])


def get_latest_day(year: int) -> int:
    return max([folder.split('-')[1].split('.py')[0] for folder in os.listdir(os.path.join('aoc', f'year-{year}')) if folder.startswith('day-')])


LATEST_YEAR = get_latest_year()


def import_day(year: int, day: int):
    return import_module_from_path('day', f'aoc/year-{year}/day-{day}.py')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--year', type=int, default=LATEST_YEAR)
    parser.add_argument('--day', type=int, default=None)
    parser.add_argument('--part', type=int, default=None)
    parser.add_argument('--number_of_runs', type=int, default=100)
    args = parser.parse_args()
    if args.day is None:
        args.day = get_latest_day(args.year)
    return args


def get_data(year: int, day: int) -> str:
    if not os.path.isfile(f'data/year-{year}/day-{day}.txt'):
        download_input(year, day)
    with open(f'data/year-{year}/day-{day}.txt') as f:
        lines = f.read()[:-1]
    return lines


def timer(part: int, func: Callable[int, str], input: str, number_of_runs: int = 100):
    time = 1
    main_start = timeit.default_timer()
    for _ in range(number_of_runs):
        start = timeit.default_timer()
        result = func(input)
        end = timeit.default_timer()
        if (t := (end - start)) < time:
            time = t
    main_end = timeit.default_timer()
    print(f"{func.__name__}: {result} ({((main_end - main_start)/number_of_runs)*1_000_000:.1f} microseconds) (min {time*1_000_000:.1f} microseconds)")
    return (main_end - main_start)/number_of_runs


def main():
    args = parse_args()
    day = import_day(args.year, args.day)
    data = get_data(args.year, args.day)
    time = 0
    if args.part == 1 or args.part is None:
        time += timer(1, day.part1, data, args.number_of_runs)
    if args.part == 2 or args.part is None:
        time += timer(2, day.part2, data, args.number_of_runs)
    print(f'Total average time: {time:.3f}s')


main()

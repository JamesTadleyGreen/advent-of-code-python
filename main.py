import argparse
import os

from timer import timer
from importer import import_module_from_path
from input import download_input


def get_latest_year() -> int:
    return max([int(folder.split("-")[1]) for folder in os.listdir("aoc")])


def get_latest_day(year: int) -> int:
    return max(
        [
            int(folder.split("-")[1].split(".py")[0])
            for folder in os.listdir(os.path.join("aoc", f"year-{year}"))
            if folder.startswith("day-")
        ]
    )


LATEST_YEAR = get_latest_year()


def import_day(year: int, day: int):
    return import_module_from_path("day", f"aoc/year-{year}/day-{day}.py")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, default=LATEST_YEAR)
    parser.add_argument("--day", type=int, default=None)
    parser.add_argument("--part", type=int, default=None)
    parser.add_argument("--number_of_runs", type=int, default=None)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    if args.day is None:
        args.day = get_latest_day(args.year)
    return args


def get_data(year: int, day: int) -> str:
    if not os.path.isfile(f"data/year-{year}/day-{day}.txt"):
        download_input(year, day)
    with open(f"data/year-{year}/day-{day}.txt") as f:
        lines = f.read()[:-1]
    return lines


def main():
    args = parse_args()
    day = import_day(args.year, args.day)
    data = get_data(args.year, args.day)
    time = 0
    if args.part == 1 or args.part is None:
        if args.test:
            print("Part 1:", day.part1(data))
        else:
            time += timer(day.part1, data, args.number_of_runs)
    if args.part == 2 or args.part is None:
        if args.test:
            print("Part 2:", day.part2(data))
        else:
            time += timer(day.part2, data, args.number_of_runs)
    print(f"Total average time: {time*1_000:.1f}ms")


main()

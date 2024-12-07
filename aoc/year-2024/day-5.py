from functools import cmp_to_key
from collections import defaultdict


def parse_input(input: str) -> tuple[defaultdict[str, set[str]], list[list[str]]]:
    order, pages = input.split("\n\n")
    d = defaultdict(set)
    for o in order.splitlines():
        l, u = o.split("|")
        d[u].add(l)
    return d, [i.split(",") for i in pages.splitlines()]


def is_ordered(pages: list[str], ordered_dict: defaultdict[str, set[str]]) -> bool:
    for i, page in enumerate(pages):
        if not set(pages[i:]).isdisjoint(ordered_dict[page]):
            return False
    return True


def middle_page(pages: list[str]) -> int:
    return int(pages[len(pages) // 2])


def part1(inp: str) -> int:
    acc = 0
    ordered_dict, pages_list = parse_input(inp)
    for pages in pages_list:
        if is_ordered(pages, ordered_dict):
            acc += middle_page(pages)
    return acc


def page_sort(order: defaultdict[str, set[str]], p1: str, p2: str) -> int:
    if p2 in order[p1]:
        return -1
    return 1


def part2(inp: str) -> int:
    acc = 0
    ordered_dict, pages_list = parse_input(inp)
    for pages in pages_list:
        if not is_ordered(pages, ordered_dict):
            ordered_pages = sorted(
                pages, key=cmp_to_key(lambda p1, p2: page_sort(ordered_dict, p1, p2))
            )
            acc += middle_page(ordered_pages)
    return acc

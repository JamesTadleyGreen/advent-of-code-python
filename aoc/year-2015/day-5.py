DISSALLOWED_WORDS = ["ab", "cd", "pq", "xy"]


def vowel_count(s: str) -> int:
    acc = 0
    for vowel in "aeiou":
        acc += s.count(vowel)
    return acc


def double_letter(s: str) -> bool:
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            return True
    return False


def is_nice(s: str) -> bool:
    for dissalowed_word in DISSALLOWED_WORDS:
        if dissalowed_word in s:
            return False
    if vowel_count(s) < 3:
        return False
    if not double_letter(s):
        return False
    return True


def part1(input: str) -> int:
    acc = 0
    for s in input.split("\n"):
        if is_nice(s):
            acc += 1
    return acc


def paired_letters(s: str) -> bool:
    for i in range(1, len(s)):
        pair, check = s[i - 1 : i + 1], s[i + 1 :]
        if pair in check:
            return True
    return False


def between_letter(s: str) -> bool:
    for i in range(2, len(s)):
        if s[i - 2] == s[i]:
            return True
    return False


def is_nice_v2(s: str) -> bool:
    if paired_letters(s) and between_letter(s):
        return True
    return False


def part2(input: str) -> int:
    acc = 0
    for s in input.split("\n"):
        if is_nice_v2(s):
            acc += 1
    return acc

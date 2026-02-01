# =========================
# 1. Рядки (Strings)
# =========================

def string_length(s: str) -> int:
    return len(s)


def concat_strings(s1: str, s2: str) -> str:
    return s1 + s2


# =========================
# 2. Числа (Int/float)
# =========================

def square_number(n: float) -> float:
    return n ** 2


def sum_numbers(a: float, b: float) -> float:
    return a + b


def divide_with_remainder(a: int, b: int) -> tuple:
    return a // b, a % b


# =========================
# 3. Списки (Lists)
# =========================

def average_list(numbers: list) -> float:
    return sum(numbers) / len(numbers)


def common_elements(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))


# =========================
# 4. Словники (Dictionaries)
# =========================

def print_dict_keys(d: dict) -> None:
    for key in d:
        print(key)


def merge_dicts(d1: dict, d2: dict) -> dict:
    return d1 | d2


# =========================
# 5. Множини (Sets)
# =========================

def union_sets(set1: set, set2: set) -> set:
    return set1 | set2


def is_subset(set1: set, set2: set) -> bool:
    return set1.issubset(set2)


# =========================
# 6. Умови та цикли
# =========================

def even_or_odd(n: int) -> str:
    return "Парне" if n % 2 == 0 else "Непарне"


def only_even(numbers: list) -> list:
    return [n for n in numbers if n % 2 == 0]


# =========================
# 7. Lambda
# =========================

even_lambda = lambda x: "парне" if x % 2 == 0 else "не парне"


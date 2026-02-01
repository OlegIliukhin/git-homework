# ====== 1. Рядки (Strings) ======

def string_length(s: str) -> int:
    return len(s)


def combine_strings(s1: str, s2: str) -> str:
    return s1 + s2


# ====== 2. Числа (Int / Float) ======

def square_number(n: float) -> float:
    return n ** 2


def sum_numbers(a: float, b: float) -> float:
    return a + b


def divide_int(a: int, b: int):
    whole = a // b      # ціла частина
    remainder = a % b  # залишок
    return whole, remainder


# ====== 3. Списки (Lists) ======

def average_list(numbers: list) -> float:
    return sum(numbers) / len(numbers)


def common_elements(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))


# ====== 4. Словники (Dictionaries) ======

def print_keys(d: dict):
    for key in d.keys():
        print(key)


def merge_dicts(d1: dict, d2: dict) -> dict:
    return d1 | d2   # об'єднання словників (Python 3.9+)


# ====== 5. Множини (Sets) ======

def union_sets(set1: set, set2: set) -> set:
    return set1 | set2


def is_subset(set1: set, set2: set) -> bool:
    return set1.issubset(set2)


# ====== 6. Умовні вирази та цикли ======

def even_or_odd(n: int):
    if n % 2 == 0:
        return "Парне"
    else:
        return "Непарне"


def only_even(numbers: list) -> list:
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result


# ====== 7. Лямбда-функція ======

is_even_lambda = lambda x: "парне" if x % 2 == 0 else "не парне"


# ====== Перевірка роботи функцій ======

if __name__ == "__main__":
    print(string_length("hello"))
    print(combine_strings("hi ", "world"))

    print(square_number(5))
    print(sum_numbers(3, 4))
    print(divide_int(10, 3))

    print(average_list([1, 2, 3, 4, 5]))
    print(common_elements([1, 2, 3], [2, 3, 4]))

    print_keys({"a": 1, "b": 2})
    print(merge_dicts({"a": 1}, {"b": 2}))

    print(union_sets({1, 2}, {2, 3}))
    print(is_subset({1, 2}, {1, 2, 3}))

    print(even_or_odd(5))
    print(only_even([1, 2, 3, 4, 5, 6]))

    print(is_even_lambda(10))
    print(is_even_lambda(7))


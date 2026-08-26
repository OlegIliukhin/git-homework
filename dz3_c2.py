# ДЗ 3.1. Робота з типами даних
#переписал функції check_even, get_even_numbers, common_elements

# ============================================================
# 1. РЯДКИ (STRINGS)
# ============================================================

# 1.1. Довжина рядка
def string_length(text):
    return len(text)


# 1.2. Об'єднання двох рядків
def concat_strings(text1, text2):
    return text1 + text2


# ============================================================
# 2. ЧИСЛА (INT / FLOAT)
# ============================================================

# 2.1. Квадрат числа
def square(number):
    return number ** 2


# 2.2. Сума двох чисел
def add_numbers(a, b):
    return a + b


# 2.3. Ціла частина та залишок від ділення
def divide_int(a, b):
    return a // b, a % b


# ============================================================
# 3. СПИСКИ (LISTS)
# ============================================================

# 3.1. Середнє значення списку
def average(numbers):
    return sum(numbers) / len(numbers)


# 3.2. Спільні елементи двох списків
def common_elements(list1, list2):
    result = []

    for item in list1:
        if item in list2:
            result.append(item)

    return result

#### переписал функції common_elements

def common_elements_new(list1: list[int], list2: list[int]) -> list[int]:
    """Повертае спільні елементи двох списків."""
    return [item for item in list1 if item in list2]

a_new = [7, 8, 9, 5]
b_new = [2, 7, 3, 8]


# ============================================================
# 4. СЛОВНИКИ (DICTIONARIES)
# ============================================================

# 4.1. Вивести всі ключі словника
def print_keys(data):
    for key in data:
        print(key)


# 4.2. Об'єднати два словники
def merge_dicts(dict1, dict2):
    return dict1 | dict2


# ============================================================
# 5. МНОЖИНИ (SETS)
# ============================================================

# 5.1. Об'єднання двох множин
def union_sets(set1, set2):
    return set1 | set2


# 5.2. Перевірка, чи є одна множина підмножиною іншої
def is_subset(set1, set2):
    return set1.issubset(set2)


# ============================================================
# 6. УМОВНІ ВИРАЗИ ТА ЦИКЛИ
# ============================================================

# 6.1. Перевірка числа на парність
def check_even(number):
    if number % 2 == 0:
        print("Парне")
    else:
        print("Непарне")

#### переписал функції check_even

def check_even_new(number: int) -> str:
    """Повертає 'Парне' або 'Непарне' залежно від числа."""
    return "Парне" if number % 2 == 0 else "Непарне"


# 6.2. Список тільки парних чисел
def get_even_numbers(numbers):
    result = []

    for number in numbers:
        if number % 2 == 0:
            result.append(number)

    return result

####переписал функції  get_even_numbers

def get_even_numbers_new(numbers: list[int]) -> list[int]:
    """Повертає список тільки з парних чисел."""
    return [number for number in numbers if number % 2 == 0]



# ============================================================
# 7. LAMBDA
# ============================================================

# 7.1. Визначення парного / непарного числа
is_even = lambda number: "парне" if number % 2 == 0 else "не парне"


# ============================================================
# ПЕРЕВІРКА РОБОТИ
# ============================================================

print("1.1:", string_length("Python"))
print("1.2:", concat_strings("Hello ", "Oleg"))

print("2.1:", square(5))
print("2.2:", add_numbers(10, 20))
print("2.3:", divide_int(17, 5))

print("3.1:", average([10, 20, 30]))

print("3.2:", common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
print("3.2 (исправленный варіант):", common_elements_new(a_new, b_new))

print("4.1:")
print_keys({"name": "Oleg", "age": 49, "city": "Dnipro"})

print("4.2:", merge_dicts(
    {"name": "Oleg", "age": 49},
    {"city": "Dnipro", "job": "Python"}))

print("5.1:", union_sets({1, 2, 3}, {3, 4, 5}))
print("5.2:", is_subset({1, 2}, {1, 2, 3}))

print("6.1:") 
check_even(8)
print("6.1 (переписанный варіант):", check_even_new(8))

print("6.2:", get_even_numbers([1, 2, 3, 4, 5, 6]))
print("6.2 (переписанный вариант):", get_even_numbers_new([1, 2, 3, 4, 5, 6]))

print("7.1:", is_even(7))
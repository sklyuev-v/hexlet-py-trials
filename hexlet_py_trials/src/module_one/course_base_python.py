import math


# Испытание 1
# Реализуйте функцию invert_case(), которая меняет в
# строке регистр каждой буквы на противоположный.

def invert_case(string: str) -> str:
    result = ''
    for symbol in string:
        if symbol == symbol.lower():
            result += symbol.upper()
        else:
            result += symbol.lower()

    return result


# Испытание 2
# В этом испытании вы будете работать с «тройками» — кортежами из трех
# элементов. Вам предстоит реализовать две функции, которые вращают тройку
# (кортеж) влево и вправо.

def rotate_left(elements: tuple) -> tuple:
    if not elements:
        return ()
    elements = list(elements)
    elements.append(elements.pop(0))
    return tuple(elements)


def rotate_right(elements: tuple) -> tuple:
    if not elements:
        return ()
    elements = list(elements)
    elements.insert(0, elements.pop())
    return tuple(elements)

# Испытание 3
# Реализуйте функцию is_perfect(), которая принимает число и возвращает True,
# если оно совершенное, и False — в ином случае.
# Совершенное число — это положительное целое число, равное сумме его
# положительных делителей (не считая само число).


def is_perfect(n: int) -> bool:
    return True if sum([d for d in range(1, n) if n % d == 0]) == n else False


# Испытание 4
# Реализуйте функцию is_power_of_three(), которая определяет,
# является ли переданное число натуральной степенью тройки.


def is_power_of_three(number: int) -> bool:
    return math.log(number, 3).is_integer()

# Испытание 5
# Реализуйте функцию fizz_buzz, которая возвращает строку с числами
# (через пробел) в диапазоне от begin до end включительно. При этом:
# Если число делится без остатка на 3, то вместо него выводится слово Fizz
# Если число делится без остатка на 5, то вместо него выводится слово Buzz
# Если число делится без остатка и на 3, и на 5, то вместо числа выводится
# слово FizzBuzz
# В остальных случаях в строку добавляется само число
# Функция принимает параметры begin и end, которые определяют начало и конец
# диапазона включительно. Функция возвращает пустую строку, если диапазон пуст
# — в случае, когда begin > end.


def fizz_buzz(begin: int, end: int) -> str:
    if begin > end:
        return ''
    result = []
    for num in range(begin, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            result.append('FizzBuzz')
        elif num % 3 == 0:
            result.append('Fizz')
        elif num % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(num))
    return ' '.join(result)


# Испытание 6
# В рамках этого испытания вы реализуете небольшой набор функций, работающих с
# отрезками прямых на двухмерной плоскости. Отрезок в нашем случае будет
# кодироваться в виде пары пар и выглядеть как-то так: ((x1, y1), (x2, y2))
# (вложенные пары — это концы отрезка). Вам нужно реализовать четыре функции:
# is_degenerated() должна возвращать истину, если отрезок вырожден в точку
# is_vertical() должна возвращать истину, если отрезок — вертикальный
# is_horizontal() должна возвращать истину, если отрезок — горизонтальный
# is_inclined() должна возвращать истину, если отрезок — наклонный


def is_degenerated(p_one: tuple, p_two: tuple) -> bool:
    return p_one == p_two


def is_vertical(p_one: tuple, p_two: tuple) -> bool:
    return p_one[0] == p_two[0] and not is_degenerated(p_one, p_two)


def is_horizontal(p_one: tuple, p_two: tuple) -> bool:
    return p_one[1] == p_two[1] and not is_degenerated(p_one, p_two)


def is_inclined(p_one: tuple, p_two: tuple) -> bool:
    return not is_vertical(p_one, p_two) and not is_horizontal(p_one, p_two)


# Испытание 7
# Реализуйте функцию is_happy_ticket(), проверяющую является ли номер
# счастливым (номер — всегда строка). Функция должна возвращать True, если
# билет счастливый, или False, если нет.
# Подразумевается, что данные на входе всегда корректны, поэтому дополнительные
# проверки не требуются.


def is_happy_ticket(ticket: str) -> bool:
    mid = len(ticket) // 2
    left = [int(x) for x in ticket[:mid].strip()]
    right =[int(x) for x in ticket[mid:].strip()]
    return sum(left) == sum(right)


# Испытание 8
# Реализуйте функцию binary_sum(), которая принимает на вход два двоичных числа
# виде строк и возвращает их сумму. Вычисленная сумма также должна быть
# бинарным числом в виде строки


def binary_sum(b_one: str, b_two: str) -> str:
    return f'{int(b_one, 2) + int(b_two, 2):b}'


# Испытание 9
# Назовем счастливыми те числа, сумма квадратов цифр которого, в результате
# ряда преобразований, превратятся в единицу.
# Реализуйте функцию is_happy_number(), которая возвращает True, если число
# счастливое, и False — если нет. Количество итераций процесса поиска
# необходимо ограничить числом 10.


def is_happy_number(number: int) -> bool:
    def sum_of_squares_digits(number: int) -> int:
        return sum([int(x) ** 2 for x in str(number)])
    
    for i in range(10):
        temp_num = sum_of_squares_digits(number)
        if temp_num == 1:
            return True
        number = temp_num
    return False


# Испытание 10
# Вам предстоит написать программу, которая шифрует сообщения по следующему
# алгоритму: она берёт текст и переставляет в нем каждые два подряд идущих
# символа.
# Если количество символов нечетное, то последний символ остается на своем
# месте:
# Реализуйте функцию encrypt(), который принимает на вход исходное сообщение и
# возвращает зашифрованное.


def encrypt(string: str) -> str:
    result = ''
    for i in range(0, len(string), 2):
        result += string[i:i+2:][::-1] 
    return result


# Испытание 11
# Реализуйте функцию fib(), находящую положительные Числа Фибоначчи. Аргументом
# функции является порядковый номер числа.


# def fib(n: int) -> int:
#     fib_num = 0
#     first = 0
#     second = 1

#     for _ in range(1, n):
#         fib_num = first + second
#         first = second
#         second = fib_num
#     return fib_num

def fib(n):
    if n <= 0: return 0
    if n == 1: return 1
    if n > 1: return fib(n - 1) + fib(n - 2)


# Испытание 12
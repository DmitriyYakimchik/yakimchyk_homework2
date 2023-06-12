# Dzmitry Yakimchyk
# Date: 06/05/2023
# Description: Homework 2
# Grodno IT Academy Python 3.11


import re

from math import sqrt
from decimal import Decimal


# Объяснение работы с функциями:
# формат определения функции (то есть: мы ее создаем) - def func(arg1, arg2, arg3)
# arg1, arg2, arg3 - это аргументы, которые передаются в функцию при ее вызове (то есть, мы ее запускаем)

# оценивается: чистота кода, наличие комментариев (PEP8), прохождение всех тестов
# нельзя менять названия функций/файлов

# пример названия репозитория для гитхаба: kazukevich_homework2 добавьте в репозиторий с домашним задание файл readme
# с датой сдачи, фамилией и именем выполнившего и кратким описанием каждой задачи (коротко, что использовали,
# алгоритм функции), оформленным в стиле markdown


def common_price(m: int, n: int, s: int, l: int) -> bool | str:
    # Напишите программу, ĸоторая считает общую цену.
    # Вводится m рублей и n ĸопееĸ цена, а таĸже ĸоличество s товара.
    # Посчитайте общую цену в рублях и ĸопейĸах за l товаров.
    # Уточнение:
    # Используйте функцию return чтобы ответ был в рублях и копейках.
    # Ответ должен быть в формате: "Общая цена составляет M рублей и N копеек за L товаров"
    if type(m) != int or type(n) != int or type(s) != int or type(l) != int:
        print('Type error')
        return False
    elif l == 0:
        print('Zero goods')
        return f"Общая цена составляет {0} рублей и {0} копеек за {0} товаров"
    elif (m <= 0 and n <= 0) or s <= 0 or l < 0:
        print('Negative price')
        return False
    else:
        # получение цены в копейках
        if m > 0:
            n += m * 100
            m = 0
        # # стоимость за 1
        # n /= s
        # # итоговая стоимость
        # n *= l
        # можно попробовать округление с использованием коэффициента l/s

        n *= Decimal(l) / Decimal(s)
        print(n)
        # получение нормального отображения цены
        if n >= 100:
            m = int(n / 100)
            n = n % 100
        n = round(n)
    return "Общая цена составляет " + str(m) + " рублей и " + str(n) + " копеек за " + str(l) + " товаров"


def triangle(a, b, c) -> bool | float:
    # Даны: три стороны треугольника.
    # Требуется: проверить, действительно ли это стороны треугольника.
    # Если стороны определяют треугольник, найти его площадь с точностью до четырёх десятичных.
    # Пример: если строны треугольника равны 2, 2, 2 то мы должны вернуть 1.7321
    # Если нет, вывести False.
    # Бонусом - с правильным возвратом мы ещё получим обьяснение в консоль почему это не треугольник.
    if type(a) == str or type(b) == str or type(c) == str:
        return False
    elif a <= 0 or b <= 0 or c <= 0:
        print('Сторона не может быть меньше или равна 0')
        return False
    else:
        if a >= b + c and b >= a + c and c >= a + b:
            print('Сторона треугольника должна быть меньше суммы двух других сторон')
            return False
        else:
            p = (a + b + c) / 2
            result = sqrt(p * (p - a) * (p - b) * (p - c))
            return round(result, 4)


def longest_word(sentence: str) -> bool | str:
    # Найти самое длинное слово в введенном предложении.
    # Учтите что в предложении могут быть знаки препинания.
    # Пример: если введено "This is a sample sentence where the longest word is in the middle!",
    # то надо вернуть "sentence"
    """Для решения задачи понадобится функция, определяющая МАКСимальный элемент из нескольких (у
    этой функции есть КЛЮЧ, который определяет, по какому параметру мы будем выбирать максимальный объект)

    Чтобы соблюсти условие по знакам препинания (выбрать только слова) - ооочень рекомендую использовать РЕГУЛЯРНЫЕ
    ВЫРАЖЕНИЯ (модуль re). Ссылку на инструкцию по ним я оставлю в информационном разделе. Если не получается
    самостоятельно найти подходящую команду - напишите мне"""
    if sentence and type(sentence) == str:
        words = list()
        # Запись регулярного выражения (Всё, кроме больших и малых букв)
        regular_string = r'[^A-z]'

        for i in list(sentence.split()):
            i = re.sub(regular_string, "", i)
            words.append(i)
        words.reverse()
        return max(words, key=len)
    else:
        return False


def uniques(repeating_string: str) -> bool | str:
    # Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
    # Например, если было введено "abc cde def", то должно быть выведено "abcdef".
    if repeating_string and type(repeating_string) == str:
        result = list()
        for i in repeating_string.replace(' ', ''):
            if i not in result:
                result.append(i)
        return ''.join(result)
    else:
        return False


def count_string_capitalization(mixed_string: str) -> bool | str:
    # Посчитать количество строчных (маленьких) и прописных (больших) букв во введенной строке.
    # Проверка рассчитана только на английские буквы.
    if type(mixed_string) != str:
        return False
    else:
        # Upper
        upp = 0
        # Lower
        low = 0
        # Регулярные выражения решил не использовать для этой задачи
        for i in mixed_string:
            if i.isupper():
                upp += 1
            elif i.islower():
                low += 1
        return f"В строке '{mixed_string}' {upp} большие и {low} маленькие буквы"

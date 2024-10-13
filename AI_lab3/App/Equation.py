"""
Модуль для решения квадратного уравнения.
Использует дискриминант для нахождения корней.
"""

import math


def solve_quadratic(a_coefficient, b_coefficient, c_coefficient):
    """
    Решает квадратное уравнение вида ax^2 + bx + c = 0.
    Возвращает корни уравнения или сообщение о невозможности их нахождения.

    Параметры:
    a_coefficient (float): Коэффициент a.
    b_coefficient (float): Коэффициент b.
    c_coefficient (float): Коэффициент c.

    Возвращает:
    str: Строка с результатом решения уравнения.
    """
    # Проверка коэффициента a (если a = 0, уравнение становится линейным)
    if a_coefficient == 0:
        if b_coefficient == 0:
            if c_coefficient == 0:
                return "Бесконечное количество решений."
            return "Решений нет."
        return f"Линейное уравнение, корень: {-c_coefficient / b_coefficient}"

    # Вычисляем дискриминант
    discriminant = b_coefficient ** 2 - 4 * a_coefficient * c_coefficient

    if discriminant > 0:
        root1 = (-b_coefficient + math.sqrt(discriminant)) / (2 * a_coefficient)
        root2 = (-b_coefficient - math.sqrt(discriminant)) / (2 * a_coefficient)
        return f"Два корня: {root1} и {root2}"
    if discriminant == 0:
        root = -b_coefficient / (2 * a_coefficient)
        return f"Один корень: {root}"
    return "Нет вещественных корней."


def main():
    """
    Запрашивает у пользователя коэффициенты для квадратного уравнения и выводит результат решения.
    """
    try:
        a_coefficient = float(input("Введите коэффициент a: "))
        b_coefficient = float(input("Введите коэффициент b: "))
        c_coefficient = float(input("Введите коэффициент c: "))
    except ValueError:
        print("Ошибка: введите числовые значения.")
        return

    # Вызываем функцию решения квадратного уравнения и выводим результат
    result = solve_quadratic(a_coefficient, b_coefficient, c_coefficient)
    print(result)


if __name__ == "__main__":
    main()

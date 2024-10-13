"""
Модуль для определения типа треугольника по его сторонам.
"""

def determine_triangle_type(side_a, side_b, side_c):
    """
    Определяет тип треугольника на основе длин его сторон.

    Параметры:
    side_a (float): Сторона a треугольника.
    side_b (float): Сторона b треугольника.
    side_c (float): Сторона c треугольника.

    Возвращает:
    str: Тип треугольника.
    """
    if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
        return "Это не треугольник."

    if side_a == side_b == side_c:
        return "Равносторонний треугольник."
    if side_a == side_b or side_b == side_c or side_a == side_c:
        if is_right_triangle(side_a, side_b, side_c):
            return "Равнобедренный прямоугольный треугольник."
        return "Равнобедренный треугольник."
    if is_right_triangle(side_a, side_b, side_c):
        return "Разносторонний прямоугольный треугольник."
    return "Разносторонний треугольник."


def is_right_triangle(side_a, side_b, side_c):
    """
    Проверяет, является ли треугольник прямоугольным.

    Параметры:
    side_a (float): Сторона a треугольника.
    side_b (float): Сторона b треугольника.
    side_c (float): Сторона c треугольника.

    Возвращает:
    bool: True, если треугольник прямоугольный, False в противном случае.
    """
    sides = sorted([side_a, side_b, side_c])
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2


def main():
    """
    Запрашивает у пользователя стороны треугольника и выводит его тип.
    """
    try:
        side_a = float(input("Введите сторону a: "))
        side_b = float(input("Введите сторону b: "))
        side_c = float(input("Введите сторону c: "))
    except ValueError:
        print("Ошибка: Введите числовые значения.")
        return

    triangle_type = determine_triangle_type(side_a, side_b, side_c)
    print(triangle_type)


if __name__ == "__main__":
    main()

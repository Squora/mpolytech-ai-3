"""
Модуль для табулирования функции y = x^2 + x на заданном интервале.
"""

def tabulate_function(start_a, end_b, step_h):
    """
    Табулирует функцию y = x^2 + x на интервале [start_a, end_b] с шагом step_h.

    Параметры:
    start_a (float): Начальное значение интервала.
    end_b (float): Конечное значение интервала.
    step_h (float): Шаг табуляции.

    Вывод:
    Таблица значений функции y = x^2 + x.
    """
    print(f"{'x':>10} | {'f(x)':>10}")
    print("-" * 25)

    x_value = start_a
    while x_value <= end_b:
        y_value = x_value ** 2 + x_value
        print(f"{x_value:>10.2f} | {y_value:>10.2f}")
        x_value += step_h


def main():
    """
    Запрашивает у пользователя параметры для табуляции и вызывает функцию
    для вывода табличных данных.
    """
    try:
        start_a = float(input("Введите начальное значение A: "))
        end_b = float(input("Введите конечное значение B: "))
        step_h = float(input("Введите шаг H: "))

        if step_h <= 0:
            print("Ошибка: Шаг должен быть положительным.")
            return

        tabulate_function(start_a, end_b, step_h)

    except ValueError:
        print("Ошибка: Введите корректные числовые значения.")


if __name__ == "__main__":
    main()

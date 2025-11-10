import re


def calculate(expression):
    """Безопасное вычисление мат выражения"""
    try:
        if not re.match(r'^[0-9+\-*/().\s]+$', expression):
            return "Ошибка: Недопустимые символы в выражении"

        result = eval(expression)
        return f"Результат: {result}"

    except ZeroDivisionError:
        return "Ошибка: Деление на ноль"
    except Exception as e:
        return f"Ошибка: Некорректное выражение - {str(e)}"


if __name__ == "__main__":
    print("Калькулятор запущен. Введите exit для выхода.")

    while True:
        expression = input("Введите выражение: ").strip()

        if expression.lower() == 'exit':
            break

        if expression:
            print(calculate(expression))
        else:
            print("Введите математическое выражение")
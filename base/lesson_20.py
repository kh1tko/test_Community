# Створіть файл, в якому будуть дві функції: multiply(a, b)
# для множення чисел та divide(a, b) для ділення. Імпортуйте ці функції у основний
# файл та використайте їх для обчислення результатів для чисел 10 та 2.

def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return f'ZeroDivisionError: division by'


def kg_to_lb(kg=100):
    return kg * 2.20462


def lb_to_kg(lb=100):
    return lb / 2.20462

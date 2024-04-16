# Задача 1
# Написати цикл for, який обраховує суму всіх чисел у списку
numbers = [1, 2, 3, 4, 5]
total = 0
for i in numbers:
    total = total + i
print(total)
# Задача 2
# Використовуючи цикл for, напишіть код, який ітерує по списку numbers = [-2, -1, 0, 1, 2] і виводить тільки позитивні числа.
numbers_b = [-2, -1, 0, 1, 2]
for i in numbers_b:
    if i > 0:
        print(i)
# Задача 3
# Використовуючи цикл for, створіть новий список, що містить квадрати всіх чисел у вихідному списку
numbers_c = [1, 2, 3, 4, 5]
list_squares = []
for i in numbers_c:
    list_squares.append(i ** 2)
print(list_squares)

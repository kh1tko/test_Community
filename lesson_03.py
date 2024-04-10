# Задача 1:
# Попросіть користувача ввести рядок і перевірте, чи є заданий рядок порожнім, конвертувавши його в булеве значення.

# answer_string = bool(input('Enter your string: '))
# assert answer_string == True, 'Empty string'

# Задача 2:
# Попросіть користувача ввести три числа, які в сумі дають 100, і перевірте це за допомогою assert.
# Якщо користувач ввів неправильно, виведіть йому помилку з написом на ваш розсуд.

# sum_of_three_numbers = (input('Enter three numbers separated by commas: '))
# sum_numbers = sum_of_three_numbers.split(', ')
# print(sum_numbers)
# sum_numbers_ = []
# for i in sum_numbers:
#     sum_numbers_.append(int(i))
# print(sum_numbers_)
# assert sum(sum_numbers_) == 100, 'Sum not one hundred'

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))
assert a + b + c == 100, 'Wrong answer'

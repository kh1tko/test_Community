# Створіть 2 списки з декількома різними словами.Об'єднайте їх за допомогою вивчених методів. Виведіть кожне слово,
# до кожного слова вказівник на його довжину (кількість символів) у форматі: "слово (довжина)".
# Використайте цикл for для цього.

list1 = ["apple", "banana", "cherry"]
list2 = ["orange", "grape", "lemon"]

list1.extend(list2)

for word in list1:
    formatted_word = f"{word} ({len(word)})"
    print(formatted_word)

# Створіть список grades зі значеннями оцінок (наприклад, 5, 3, 4, 2, 5).
# Видаліть всі низькі оцінки (менше або рівно 3) за допомогою циклу та відсортуйте. Виведіть оновлений список.
new_numbers = []
numbers = [99, 29, 399, 745, 75, 1, 2, 8, 9]
for i in numbers:
    if i >= 3:
        new_numbers.append(i)
new_numbers.sort()
print(new_numbers)

# Створити список (наприклад такий ["apple", "grape", "kiwi", "pear", "melon", "banana", "mango"]).
# За допомогою методу із відео на уроці відсортуйте список за зростанням довжини слів та зробіть вивід на екран.
fruits = ["apple", "grape", "kiwi", "pear", "melon", "banana", "mango"]
fruits.sort(key=len)
print(fruits)
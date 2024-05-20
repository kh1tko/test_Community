# d = {'name': 'John Doe', 'age': 30, 'city': 'New York', 'email': 'johndoe@example.com'}
# # Попросіть користувача ввести ключ, який він бажає видалити, і видаліть цей елемент зі словника.
# a = 'email'
# d.pop(a)
# print(d)


# d = {'name': 'Alice Smith', 'age': 25, 'city': 'Los Angeles', 'email': 'alice.smith@example.com',
#      'favorite_subjects': ['Mathematics', 'History', 'Literature']
#      }
# # Виведіть з цього списку значення улюблених предметів використовуючи цикл
#
# for k in d.get('favorite_subjects'):
#     print(k)

# Видаліть з цього списку sports та додайте новий ключ 'serials' де значенням будуть ваші улюблені серіали.
favorites = {
    'movies': ['Interstellar', 'Fast & Furious', 'Pirates of the Caribbean'],
    'music': ['Queen', 'The Beatles', 'Coldplay'],
    'sports': ['football', 'basketball', 'tennis']
}

favorites.pop('sports')
favorites.update({'serials': ['Game of throne', 'Breaking bad', 'Office']})
print(favorites)

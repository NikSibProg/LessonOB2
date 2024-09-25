class User:
    def __init__(self, user_id, name):
        # Инициализация атрибутов пользователя
        self.__user_id = user_id  # Уникальный идентификатор пользователя
        self.__name = name        # Имя пользователя
        self.__access_level = 'user'  # Уровень доступа (обычный пользователь)

    # Метод для получения уникального идентификатора пользователя
    def get_user_id(self):
        return self.__user_id

    # Метод для получения имени пользователя
    def get_name(self):
        return self.__name

    # Метод для получения уровня доступа
    def get_access_level(self):
        return self.__access_level


class Admin(User):
    def __init__(self, user_id, name):
        # Вызов конструктора родительского класса
        super().__init__(user_id, name)
        self.__access_level = 'admin'  # Уровень доступа (администратор)
        self.__user_list = []           # Список пользователей, управляемых администратором

    # Метод для добавления пользователя в список
    def add_user(self, user):
        if isinstance(user, User):  # Проверка, что переданный объект - это экземпляр User
            self.__user_list.append(user)  # Добавление пользователя в список

    # Метод для удаления пользователя из списка по уникальному идентификатору
    def remove_user(self, user_id):
        self.__user_list = [user for user in self.__user_list if user.get_user_id() != user_id]

    # Метод для получения списка имен пользователей
    def get_user_list(self):
        return [user.get_name() for user in self.__user_list]


# Пример использования классов
admin = Admin(1, 'Admin User')  # Создание объекта администратора
user1 = User(2, 'Regular User 1')  # Создание обычного пользователя
user2 = User(3, 'Regular User 2')  # Создание еще одного обычного пользователя

# Добавление пользователей в список администратором
admin.add_user(user1)
admin.add_user(user2)

# Вывод списка имен пользователей
print(admin.get_user_list())  # ['Regular User 1', 'Regular User 2']

# Удаление одного пользователя по ID
admin.remove_user(2)

# Вывод обновленного списка имен пользователей
print(admin.get_user_list())  # ['Regular User 2']

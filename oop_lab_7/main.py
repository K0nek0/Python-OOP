from enum import Enum


class Gender(Enum):
    Male = 0
    Female = 1


class User:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.email = ""
        self.phone = ""
        self.city = ""
        self.gender = Gender.Male

    def get_id(self):
        return self.id

    def set_id(self, _id):
        self.id = _id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender


class IRepository:
    def add(self, item):
        raise NotImplementedError

    def update(self, item):
        raise NotImplementedError

    def delete(self, item):
        raise NotImplementedError

    def get(self, where, order_by):
        raise NotImplementedError


class IUserRepository:
    def get_by_id(self, _id):
        raise NotImplementedError

    def get_by_name(self, name):
        raise NotImplementedError

    def get_by_email(self, email):
        raise NotImplementedError

    def get_by_city(self, city):
        raise NotImplementedError

    def get_by_gender(self, gender):
        raise NotImplementedError


class MemoryRepository(IRepository):
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def update(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                self.items[i] = item
                break

    def delete(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                del self.items[i]
                break

    def get(self, where, order_by):
        return self.items


class MemoryUserRepository(MemoryRepository, IUserRepository):
    def get_by_id(self, _id):
        for user in self.items:
            if user.get_id() == _id:
                return user
        return None

    def get_by_name(self, name):
        for user in self.items:
            if user.get_name() == name:
                return user
        return None

    def get_by_email(self, email):
        for user in self.items:
            if user.get_email() == email:
                return user
        return None

    def get_by_city(self, city):
        result = []
        for user in self.items:
            if user.get_city() == city:
                result.append(user)
        return result

    def get_by_gender(self, gender):
        result = []
        for user in self.items:
            if user.get_gender() == gender:
                result.append(user)
        return result


def main():
    repos = MemoryUserRepository()

    user1 = User()
    user1.set_id(1)
    user1.set_name("Nikolay")
    user1.set_email("nikolaytimoshchenko@mail.ru")
    user1.set_phone("8805553535")
    user1.set_city("Kaliningrad")
    user1.set_gender(Gender.Male)

    user2 = User()
    user2.set_id(2)
    user2.set_name("Yarick")
    user2.set_email("yar@yandex.ru")
    user2.set_phone("3458757293")
    user2.set_city("Paris")
    user2.set_gender(Gender.Male)

    user3 = User()
    user3.set_id(3)
    user3.set_name("Test1")
    user3.set_email("test1@pochta.ru")
    user3.set_phone("1234571543")
    user3.set_city("Testik1")
    user3.set_gender(Gender.Male)

    user4 = User()
    user4.set_id(6)
    user4.set_name("Test2")
    user4.set_email("test2@gmail.com")
    user4.set_phone("883458838")
    user4.set_city("Testik2")
    user4.set_gender(Gender.Female)

    repos.add(user1)
    repos.add(user2)
    repos.add(user3)
    repos.add(user4)

    print()
    users = repos.get("", "")
    print("All users:")
    for user in users:
        print(
            f"{user.get_id()} {user.get_name()} {user.get_email()} {user.get_phone()} {user.get_city()} {user.get_gender()}")

    print()
    user_by_id = repos.get_by_id(2)
    print("User by id 2:")
    if user_by_id is not None:
        print(
            f"{user_by_id.get_id()} {user_by_id.get_name()} {user_by_id.get_email()} {user_by_id.get_phone()} {user_by_id.get_city()} {user_by_id.get_gender()}")

    print()
    user_by_gender = repos.get_by_gender(Gender.Female)
    print(f"Female users:")
    if user_by_gender is not None:
        for user in user_by_gender:
            print(
                f"{user.get_id()} {user.get_name()} {user.get_email()} {user.get_phone()} {user.get_city()} {user.get_gender()}")


if __name__ == "__main__":
    main()

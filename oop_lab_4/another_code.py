import time


class Key:
    def __init__(self, name, action, undo_action):
        self.name = name
        self.action = action
        self.undo_action = undo_action

    def press(self):
        return self.action()

    def undo(self):
        return self.undo_action()


class Keyboard:
    def __init__(self):
        self.__keys = {} # теперь приватная переменная, т.е. доступ вне класса заблокирован
        self.__history = [] # также приватная
        self.text = ""
        self.volume = 0

    def add_key(self, key):
        self.__keys[key.name] = key

    def press(self, key_name):
        if key_name in self.__keys:
            result = self.__keys[key_name].press()
            if result:
                self.__history.append((self.__keys[key_name], result))
            self.__print_state()

    def undo(self):
        if self.__history:
            key, prev_state = self.__history.pop()
            key.undo()
            self.__print_state()

    def __print_state(self): # также играничил доступ к данному методу, чтобы пользователь не смог изменить вывод
        print(f"Текст: {self.text}")
        print(f"Громкость: {self.volume}\n")


def run():
    app = Keyboard()

    def add_letter(letter):
        app.text += letter
        return app.text

    def delete_last_letter():
        app.text = app.text[:-1]
        return app.text

    def increase_volume():
        if app.volume < 100:
            app.volume += 10
        return app.volume

    def decrease_volume():
        if app.volume > 0:
            app.volume -= 10
        return app.volume

    keys_info = {
        'a': 'Добавить букву "a"',
        'b': 'Добавить букву "b"',
        'c': 'Добавить букву "c"',
        'd': 'Добавить букву "d"',
        'e': 'Добавить букву "e"',
        'f8': 'Увеличить громкость',
        '~': 'Отменить последнее действие'
    }

    for key, description in keys_info.items():
        print(f"{key}: {description}")

    time.sleep(3)

    for letter in 'abcde':
        app.add_key(Key(letter, lambda l=letter: add_letter(l), delete_last_letter))

    app.add_key(Key("f8", increase_volume, decrease_volume))

    sequence = ['a', 'b', 'c', 'f8', 'd', 'e', '~']

    for key in sequence:
        print(f"\nНажата клавиша: {key}")
        app.press(key)
        time.sleep(2)

    app.undo()


if __name__ == "__main__":
    run()

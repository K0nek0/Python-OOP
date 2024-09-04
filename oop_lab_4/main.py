import time

CONSOLE_SIZE = 71


class Command:
    def execute(self, target_activity, volume, brightness):
        temp_volume = volume
        temp_brightness = brightness
        temp_left = []
        temp_right = []

        for key in target_activity:
            if isinstance(key.command, StringCommand):
                temp_left.append(key.key_name)

            right = str(key.command)
            if isinstance(key.command, StringCommand):
                right += "\""
                right += key.key_name
                right += "\""

            temp_right.append(right)

            if isinstance(key.command, UndoCommand) and target_activity.index(key) - 1 >= 0:
                prev_command = target_activity[target_activity.index(key) - 1].command
                if isinstance(prev_command, StringCommand):
                    temp_left.pop()
                    temp_left.pop()
                elif isinstance(prev_command, VolumeUpCommand):
                    temp_volume -= 10
                elif isinstance(prev_command, VolumeDownCommand):
                    temp_volume += 10
                elif isinstance(prev_command, BrightnessUpCommand):
                    temp_brightness -= 10
                elif isinstance(prev_command, BrightnessDownCommand):
                    temp_brightness += 10

        left = [temp_left[i:i + CONSOLE_SIZE // 2 - 1] for i in range(0, len(temp_left), CONSOLE_SIZE // 2 - 1)]
        right = [temp_right[i:i + CONSOLE_SIZE // 2 - 1] for i in range(0, len(temp_right), CONSOLE_SIZE // 2 - 1)]

        result = "-" * CONSOLE_SIZE + "\n"
        for i in range(max(len(left), len(right))):
            if i < len(left):
                result += str(left[i])
            else:
                result += " " * (CONSOLE_SIZE // 2 - 1)

            if i < len(left):
                result += " " * (CONSOLE_SIZE // 2 - 1 - len(left[i]))

            result += "|"

            if i < len(right):
                result += str(right[i])
            else:
                result += " " * (CONSOLE_SIZE // 2 - 1)

            result += "\n"

        temp = "volumeLevel:" + "    " + " " * (4 - len(str(temp_volume))) + str(temp_volume)
        result += temp
        result += " " * (CONSOLE_SIZE // 2 - 1 - len(temp))
        result += "|\n"

        temp = "brightnessLevel:" + " " * (4 - len(str(temp_brightness))) + str(temp_brightness)
        result += temp
        result += " " * (CONSOLE_SIZE // 2 - 1 - len(temp))
        result += "|\n"

        result += "-" * CONSOLE_SIZE + "\n"

        print(result)
        return temp_volume, temp_brightness


class StringCommand(Command):
    def __str__(self):
        return "PressedKey: "


class VolumeUpCommand(Command):
    def execute(self, target_activity, volume, brightness):
        super().execute(target_activity, volume + 10, brightness)
        return volume + 10, brightness

    def __str__(self):
        return "VolumeUp"


class VolumeDownCommand(Command):
    def execute(self, target_activity, volume, brightness):
        super().execute(target_activity, volume - 10, brightness)
        return volume - 10, brightness

    def __str__(self):
        return "VolumeDown"


class BrightnessUpCommand(Command):
    def execute(self, target_activity, volume, brightness):
        super().execute(target_activity, volume, brightness + 10)
        return volume, brightness + 10

    def __str__(self):
        return "BrightnessUp"


class BrightnessDownCommand(Command):
    def execute(self, target_activity, volume, brightness):
        super().execute(target_activity, volume, brightness - 10)
        return volume, brightness - 10

    def __str__(self):
        return "BrightnessDown"


class UndoCommand(Command):
    def __str__(self):
        return "Undo"


class Key:
    def __init__(self, key_name, command):
        self.key_name = key_name
        self.command = command

    def __hash__(self):
        return hash((self.key_name, self.command))


class Keyboard:
    def __init__(self):
        self.keys = set()
        self.last_activity = []
        self.brightness = 0
        self.volume = 0

    def add_key(self, new_key):
        self.keys.add(new_key)

    def press_key(self, target_key):
        if target_key in self.keys or isinstance(target_key.command, UndoCommand):
            self.last_activity.append(target_key)
            if isinstance(target_key.command, VolumeUpCommand) or isinstance(target_key.command, VolumeDownCommand):
                self.volume = target_key.command.execute(self.last_activity, self.volume, self.brightness)[0]
            elif isinstance(target_key.command, BrightnessUpCommand) or isinstance(target_key.command, BrightnessDownCommand):
                self.brightness = target_key.command.execute(self.last_activity, self.volume, self.brightness)[1]
            else:
                target_key.command.execute(self.last_activity, self.volume, self.brightness)
        else:
            raise ValueError(f"Key {target_key} not found in {self.keys}")

    def add_activity(self, key_name, command):
        temp_key = Key(key_name, command)
        self.add_key(temp_key)
        self.press_key(temp_key)

    def undo(self):
        self.press_key(Key("", UndoCommand()))


def main():
    keyboard = Keyboard()
    first_key = Key("first", StringCommand())
    second_key = Key("second", StringCommand())
    volume_key = Key("", VolumeUpCommand())
    brightness_key = Key("", BrightnessUpCommand())
    keyboard.add_key(first_key)
    keyboard.add_key(second_key)
    keyboard.add_key(volume_key)
    keyboard.add_key(brightness_key)

    keyboard.press_key(first_key)
    time.sleep(2)

    keyboard.press_key(second_key)
    time.sleep(2)

    keyboard.press_key(volume_key)
    time.sleep(2)

    keyboard.press_key(brightness_key)
    time.sleep(2)

    keyboard.press_key(volume_key)
    time.sleep(2)

    keyboard.undo()


main()

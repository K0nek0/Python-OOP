class ConsoleArt:
    def __init__(self):
        self.alphabets = {
            'standard': {
                'A': [
                    "  A  ",
                    " A A ",
                    "AAAAA",
                    "A   A",
                    "A   A",
                ],
                'B': [
                    "BBBB ",
                    "B   B",
                    "BBBB ",
                    "B   B",
                    "BBBB ",
                ],
            },
            'big': {
                'A': [
                    "   AA   ",
                    "  A  A  ",
                    " AAAAAA ",
                    "A      A",
                    "A      A",
                ],
                'B': [
                    "BBBBB  ",
                    "B    B ",
                    "BBBBBB ",
                    "B    B ",
                    "BBBBB  ",
                ],
            }
        }
        self.symbol = '*'  # символ по умолчанию
        self.current_font = 'standard'  # шрифт по умолчанию

    def set_font(self, font_name):
        if font_name in self.alphabets:
            self.current_font = font_name
        else:
            print("Шрифт не найден. Используется 'standard'.")

    def set_symbol(self, symbol):
        if symbol != '':
            self.symbol = symbol
        else:
            print("Строка пустая. Используется '*'.")

    def print_art(self, text, x=0, y=0):
        lines = [""] * len(self.alphabets[self.current_font]['A'])

        for char in text:
            if char.upper() in self.alphabets[self.current_font]:
                char_data = self.alphabets[self.current_font][char.upper()]
                for i, line in enumerate(char_data):
                    if y + i < len(lines):
                        lines[y + i] += " " * x + line.replace(char.upper(), self.symbol)
                    else:
                        break

        for line in lines:
            print(line)


if __name__ == "__main__":
    console_art = ConsoleArt()

    try:
        console_art.set_font('big') # размер шрифта
        console_art.set_symbol('0') # символ
        console_art.print_art("ABBA", 12, 0) # текст и его координаты
    except KeyboardInterrupt:
        pass

import random


class TextBox:
    def __init__(self, text="", input_position=(0, 0)):
        self.text = text
        self.position = input_position

    def __str__(self):
        return self.text


class WindowsTextBox(TextBox):
    def __str__(self):
        return "WindowsTextBox: " + self.text


class LinuxTextBox(TextBox):
    def __str__(self):
        return "LinuxTextBox: " + self.text


class AndroidTextBox(TextBox):
    def __str__(self):
        return "AndroidTextBox: " + self.text


class Control:
    def __init__(self, position=(0, 0)):
        self.position = position

    def setter_position(self, new_position):
        if new_position[0] >= 0:
            self.position = new_position

    def getter_position(self):
        return self.position


class Button(Control):
    def __init__(self, input_text="", input_position=(0, 0)):
        super().__init__(input_position)
        self.button_text = input_text

    def click(self):
        print("Clicked", self.button_text, "in", self)


class WindowsButton(Button):
    def __str__(self):
        return "WindowsButton: " + self.button_text


class LinuxButton(Button):
    def __str__(self):
        return "LinuxButton: " + self.button_text


class AndroidButton(Button):
    def __str__(self):
        return "AndroidButton: " + self.button_text


class Form(Control):
    def __init__(self, position=(0, 0)):
        super().__init__(position)
        self.elements = []

    def add_control(self, element):
        print("Added", element, "to", self)
        self.elements.append(element)


class WindowsForm(Form):
    def add_control(self, element):
        if isinstance(element, (WindowsForm, WindowsTextBox, WindowsButton)):
            super().add_control(element)

    def __str__(self):
        return "WindowsForm"


class LinuxForm(Form):
    def add_control(self, element):
        if isinstance(element, (LinuxForm, LinuxTextBox, LinuxButton)):
            super().add_control(element)

    def __str__(self):
        return "LinuxForm"


class AndroidForm(Form):
    def add_control(self, element):
        if isinstance(element, (AndroidForm, AndroidTextBox, AndroidButton)):
            super().add_control(element)

    def __str__(self):
        return "AndroidForm"


class ControlFabric:
    def create_form(self, input_position):
        return Form(input_position)

    def create_text_box(self, text="", position=(0, 0)):
        return TextBox(text, position)

    def create_button(self, input_text="", input_position=(0, 0)):
        return Button(input_text, input_position)


class WindowsFabric(ControlFabric):
    def create_form(self, input_position):
        return WindowsForm(input_position)

    def create_text_box(self, text="", position=(0, 0)):
        return WindowsTextBox(text, position)

    def create_button(self, input_text="", input_position=(0, 0)):
        return WindowsButton(input_text, input_position)


class LinuxFabric(ControlFabric):
    def create_form(self, input_position):
        return LinuxForm(input_position)

    def create_text_box(self, text="", position=(0, 0)):
        return LinuxTextBox(text, position)

    def create_button(self, input_text="", input_position=(0, 0)):
        return LinuxButton(input_text, input_position)


class AndroidFabric(ControlFabric):
    def create_form(self, input_position):
        return AndroidForm(input_position)

    def create_text_box(self, text="", position=(0, 0)):
        return AndroidTextBox(text, position)

    def create_button(self, input_text="", input_position=(0, 0)):
        return AndroidButton(input_text, input_position)


OS = ["Windows", "Linux", "Android"]
current_os = random.choice(OS)

if current_os == "Windows":
    main_form = WindowsForm((19, 0))
    main_fabric = WindowsFabric()
elif current_os == "Linux":
    main_form = LinuxForm((19, 0))
    main_fabric = LinuxFabric()
else:
    main_form = AndroidForm((19, 0))
    main_fabric = AndroidFabric()

main_form.add_control(main_fabric.create_text_box("firstText", (0, 0)))
main_form.add_control(main_fabric.create_button("button", (12, 9)))
main_form.add_control(main_fabric.create_form((76, 90)))

for control in main_form.elements:
    if isinstance(control, Button):
        control.click()

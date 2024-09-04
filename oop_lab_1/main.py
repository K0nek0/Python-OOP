import math
from abc import ABC, abstractmethod


class IntegralCalculator(ABC): # абстрактный класс
    @abstractmethod
    def calculate_integral(self, start, end, split):
        raise NotImplementedError # исключение, возникающее в случаях, когда наследник класса не переопределил метод, который должен был
        # pass # либо можно оставить "pass", в нашем случае разницы нет


def math_function(x): # объявляем нашу функцию
    return 3 * math.log(x)


class TrapezoidalMethod(IntegralCalculator): # создаем класс-наследник
    def calculate_integral(self, start, end, split):
        step = (end - start) / split
        result = 0

        for i in range(split):
            result += (math_function(start + i * step) + math_function(start + (i + 1) * step)) * step / 2
        return result


class SimpsonMethod(IntegralCalculator):
    def calculate_integral(self, start, end, split):
        step = (end - start) / split
        result = 0

        for i in range(split):
            result += ((math_function(start + i * step) + 4 * math_function(start + (i + 0.5) * step)
                        + math_function(start + (i + 1) * step)) * step / 6)
        return result


def variables(): # функция с переменными (сделана для удобства)
    start_num = 2
    end_num = 8
    split_num = 10
    step_size = (end_num - start_num) / split_num
    return start_num, end_num, split_num, step_size


if __name__ == "__main__":
    calculator = TrapezoidalMethod() # создаем экземпляр класса
    integral = calculator.calculate_integral(variables()[0], variables()[1], variables()[2]) # создаем переменную, которая принимает значение функции
    print(f"Trapezoidal Method: Integral = {integral}, Step Size = {variables()[3]}, Number of Points = {variables()[2]}")

    calculator = SimpsonMethod()
    integral = calculator.calculate_integral(variables()[0], variables()[1], variables()[2])
    print(f"Simpson Method: Integral = {integral}, Step Size = {variables()[3]}, Number of Points = {variables()[2]}")


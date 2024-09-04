class Array3d:
    def __init__(self, dim0, dim1, dim2):
        self.dim0 = dim0
        self.dim1 = dim1
        self.dim2 = dim2
        self.__size = dim0 * dim1 * dim2  # теперь мы не можем обратиться к этой переменной, поскольку она приватная
        self.__array = [0] * self.__size  # также приватная

    def index(self, i, j=None, k=None):
        return i * self.dim1 * self.dim2 + j * self.dim2 + k

    def __getitem__(self, index):
        if isinstance(index, tuple) and len(index) == 3:
            i, j, k = index
            return self.__array[self.index(i, j, k)]
        raise IndexError("Invalid index")

    def __setitem__(self, index, value):
        if isinstance(index, tuple) and len(index) == 3:
            i, j, k = index
            self.__array[self.index(i, j, k)] = value
        else:
            raise IndexError("Invalid index")

    def get_value0(self, i):
        return [[self.__array[self.index(i, j, k)] for k in range(self.dim2)] for j in range(self.dim1)]

    def get_value1(self, j):
        return [[self.__array[self.index(i, j, k)] for k in range(self.dim2)] for i in range(self.dim0)]

    def get_value2(self, k):
        return [[self.__array[self.index(i, j, k)] for j in range(self.dim1)] for i in range(self.dim0)]

    def get_value01(self, i, j):
        return [self.__array[self.index(i, j, k)] for k in range(self.dim2)]

    def get_value02(self, i, k):
        return [self.__array[self.index(i, j, k)] for j in range(self.dim1)]

    def get_value12(self, j, k):
        return [self.__array[self.index(i, j, k)] for i in range(self.dim0)]

    @staticmethod
    def create_fill(dim0, dim1, dim2, value):
        array3d = Array3d(dim0, dim1, dim2)
        array3d.__array = [value] * array3d.__size
        return array3d


# Создаем экземпляр класса Array3d
array = Array3d(3, 4, 2).create_fill(3, 4, 2, 4)
try:
    print(array.__size)  # если же мы все таки попытаемся получить/изменить значение, то получим ошибку
except:
    AttributeError

# Получаем значения из массива с помощью методов
print(f"Cрез массива по индексу i вдоль оси I: {array.get_value0(1)}")

print(f"\nCрез массива по индексу j вдоль оси J {array.get_value1(2)}")

print(f"\nCрез массива по индексу k вдоль оси K: {array.get_value2(0)}")

print(f"\nCрез массива по индексам i и j: {array.get_value01(2, 3)}")

print(f"\nCрез массива по индексам i и k: {array.get_value02(1, 0)}")

print(f"\nCрез массива по индексам j и k: {array.get_value12(2, 1)}")

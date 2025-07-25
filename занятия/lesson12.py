# Документирование функций и тайпхинты

# def do_it(param_1, param_2, param_3):
def do_it(param_1: int, param_2: str, param_3: float) -> list:  # type hint
    """
    Эта функция берет первые два параметра, складывает их и делит на
    третий.

    Результат печатается в консоль.
    Параметры должны быть в консоли.
    """
    result = (param_1 + param_2) * param_3
    print(result)


do_it(1, 2, 3)


def summa(a: int, b:float) -> None:
    print(a + b)


# Документирование классов
class MyClass:
    """
    Мой класс. С двумя аргументами (arg1, arg2) и одним методом show()
    """
    
    ATTRIBUTE1 = '1'

    def __init__(self, arg1: int, arg2: str) -> None:
        self.arg1 = arg1
        self.arg2 = arg2

    def info(self):
        """
        Вывод информации о объекте.
        """
        print(self.arg1, self.arg2)


obj = MyClass(10, "текс")
obj.info()

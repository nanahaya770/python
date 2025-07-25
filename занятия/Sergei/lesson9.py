# Функции и их аргументы

# def summ(number1, number2):
#     result = number1 + number2
#     print(result)

# summ(10, 25)


# def text():
#     print('hello')

# text()


# Функции возвращающие результат

# def summ_v2(number1, number2):
#     result = number1 + number2
#     return result

# summa = summ_v2(11, 22) * 10
# print(summa) # -> 330

# print(summ(1, 2)) # -> None

# Задание:
# Создать функцию, которая вычисляет площадь прямоугольника
# по формуле: площадь = высота * ширину, и выводит результат на экран

# def square(a, b):
#     s = a*b
#     # print(s)
#     return s


# square(3, 4)
# square(4, 6)
# summa = square(3, 4) + square(4, 6)
# print(summa)

def celsius_to_fahrenheit(celsius: float) -> float:
    fahrenheit = celsius * 9/5 + 32
    # print(fahrenheit)
    return fahrenheit


# celsius_to_fahrenheit(0)
# celsius_to_fahrenheit(100)


# def add_numbers(
#     a: (float | int),
#     b: (float | int),
#     c: (float | int)
# ) -> (float | int):
#     result = a + b + c
#     print(result)
#     return result


# add_numbers(3, 5, 0)
# add_numbers(2.5, 4.5, 1)

# def sum_temperatures_in_fahrenheit(
#     celsius_temperature1: float,
#     celsius_temperature2: float,
#     celsius_temperature3: float
# ) -> float:
#     total_fahrenheit = 0.0
#     fahrenheit1 = celsius_temperature1 * 9/5 + 32
#     fahrenheit2 = celsius_temperature2 * 9/5 + 32
#     fahrenheit3 = celsius_temperature3 * 9/5 + 32
#     total_fahrenheit = fahrenheit1 + fahrenheit2 + fahrenheit3
#     print(
#         f"{fahrenheit1} + {fahrenheit2} + {fahrenheit3} = {total_fahrenheit}"
#     )

#     return total_fahrenheit


# sum_temperatures_in_fahrenheit(0.0, 100.0, 37.0)
# sum_temperatures_in_fahrenheit(-10.0, 20.0, 30.0)


# def sum_temperatures_in_fahrenheit2(
#     celsius_temperature1: float,
#     celsius_temperature2: float,
#     celsius_temperature3: float
# ) -> float:
#     total_fahrenheit = 0.0
#     fahrenheit1 = celsius_to_fahrenheit(celsius_temperature1)  # ИЗ СТРОКИ 43
#     fahrenheit2 = celsius_to_fahrenheit(celsius_temperature2)
#     fahrenheit3 = celsius_to_fahrenheit(celsius_temperature3)
#     total_fahrenheit = fahrenheit1 + fahrenheit2 + fahrenheit3
#     print(
#         f"{fahrenheit1} + {fahrenheit2} + {fahrenheit3} = {total_fahrenheit}"
#     )

#     return total_fahrenheit


# sum_temperatures_in_fahrenheit2(0.0, 150.0, 37.0)
# sum_temperatures_in_fahrenheit2(-10.0, 20.0, 30.0)

def sum_temperatures_in_fahrenheit3(
    celsius1: float,
    celsius2: float,
    celsius3: float
) -> float:
    total_celsius = celsius1 + celsius2 + celsius3
    total_fahrenheit = celsius_to_fahrenheit(total_celsius)  # ИЗ СТРОКИ 43

    print(total_fahrenheit)

    return total_fahrenheit


sum_temperatures_in_fahrenheit3(0.0, 150.0, 37.0)
sum_temperatures_in_fahrenheit3(-10.0, 20.0, 30.0)

# Функции

# def name_function(): # def - definition
#     print("Команда 1")
#     print("Команда 2")

# name_function()


# def total_price(price): # 1000
#     result = price * (1-0.15) # 1000 * 0.85
#     print(result)

# total_price(1000)
# print("Функция выполнена 1 раз")

# total_price(100)
# print("Функция выполнена 2 раз")

# total_price(300)
# print("Функция выполнена 3 раз")

# print()


# def welcome(name):
#     print(f'Привет, {name}')

# welcome('Павел')


# Задание создать функцию которая принимает 
# число, и умножает его на 100

def calculate(number):
    result = number * 100
    print(result)


calculate(10)
calculate(111)

# Пример 1
# Исходная строка:
# Привет, Василий. Как дела?

# Результат:
# Здравсвуйте, Василий. Как дела?

# Пример 2
# Исходная строка:
# Привет, Мария. Идём гулять?

# Результат:
# Здравствуйте, Мария. Идём гулять?


def goodday(name):
    print(f'"Привет {name}! Как дела?"'. replace("Привет", "Здравствуйте"))


goodday("Василий")


def goodday(name):
    print(f'"Привет {name}. Идём гулять?"'. replace("Привет", "Здравствуйте"))


goodday("Мария")


# def word(text):
#     print(f"{text}!!!")


# word("хороший день")    

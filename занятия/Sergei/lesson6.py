# Таблица ASCII
# https://upload.wikimedia.org/wikipedia/commons/1/1b/ASCII-Table-wide.svg

# Кодировка UTF-8 (UTF-16) ...

# Ввод текста
text = "Слово" # input() # 12 14 55 11

# Сопастивать каждую букву какому-то числу

# alfabet = 'abcd'

# alfabet = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }

# Создать переменную для суммы

# В цикле получать числовое значение каждой буквы и увеличивать сумму
# for
# print(alfabet['ab'])

# ord()
# chr()
# print(ord('W'))

# print(ord('Hello'))  Error

summa = 0
for symbol in text:
    number = ord(symbol) - 1039
    summa = summa + number
    print(symbol, number)

print(summa)

# Свой словарь
# own_alfabet = {
#     'a': 1,
#     'b': 2,
#     'c': 10
# }

# print()
# for symbol in text:
#     print(symbol, own_alfabet[symbol])


# ДЗ
# 1. переделать код для своего алфавита на основе словаря dict
# 2. добавить пользовательский ввод слов с консоли

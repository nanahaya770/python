# https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python

# def positive_sum(numbers):
#     total = 0
#     # создаем переменную, для результата сложения. изначально общая сумма = 0
#     for number in numbers:
#         # цикл: из списка берет по одной цифре
#         if number > 0:  # при условии, что цифра больше 0
#             total = total + number
#             # общая сумма = предыдущая сумма + следующее положительное число
#     return total  # верни итоговую сумму


# print(positive_sum([1, -3, 7, 0, 55]))
# # выведи в терминал функцию positive_sum, если список цифр [1, -3, 7, 0, 55]

def positive_sum(numbers):
    total = 0
    for number in numbers:
        if number > 0:
            total = total + number
            print(f"{total - number} + {number} = {total}")

    return total


positive_sum([1, -3, 7, 0, 55])

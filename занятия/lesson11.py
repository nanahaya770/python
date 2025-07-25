# # Списки и методы списков

# # Создание списков
# l1 = []
# l2 = list()

# # Добавление элементов в список
# print(l2)
# l2.append(10)
# print(l2)
# l2.append("text")
# print(l2)

# # Обновление
# l2[1] = "TEXT"
# print(l2)

# # Удаление
# l2.remove(10)
# print(l2)


# # Сложение списков
# l3 = [1, 2, 3]
# l4 = ["text1", "text2"]

# print(l3 + l4)

# # Умножение списка на число
# print(l3 * 4)

# # Операции - / // % - ... недоступны


# # Методы списков
# # print(dir([]))
# # 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
# l5 = [1, 2, 50]
# l5.append("text")
# print(l5)

# l5.append(["name", "age"])
# print(l5)

# l5 = l5 + ["text1", "text2"]
# print(l5)

# # copy
# l6 = l5.copy()
# print(l6)

# # clear
# l5.clear()
# print(l5)

# # count
# print(l6.count('text1'))
# l7 = l3 * 4
# print(l7)
# print(l7.count(3))

# # Длина списка
# print(len(l6))

# names = list(['Катя', 'Маша', 'Оля', 'Юля'])
# names[2] = 'Женя'
# print(names)

# nums = [1, 2, 3, 4, 5]
# nums2 = [6, 7, 8, 9, 10]
# print(nums + nums2)

# nums3 = nums + nums2
# nums3.remove(7)
# print(nums3)


# def number_to_string(num):
#     return str(num)


# print(number_to_string(19))


# def bool_to_word(boolean):
#     if boolean == True: 
#         return "yes"
#     else:
#         return "no"


# print(bool_to_word(False))


# def square_sum(numbers):
#     num = numbers
#     for num in numbers:
#         print(num)


# square_sum([1, 2, 3])


# def square_sum(numbers):
#     sum = 0
#     num = numbers
#     for num in numbers:
#         sum = sum + num
#         print(sum)


# square_sum([1, 2, 3])

def square_sum(numbers):
    sum = 0
    num = numbers
    for num in numbers:
        sum = num**2
        print(sum)


square_sum([1, 2, 3])


# def square_sum(numbers):
#     sum = 0
#     num = numbers
#     for num in numbers:
#         sum = sum + num**2
#         print(sum)


# square_sum([1, 2, 3])


# def square_sum(numbers):
#     return sum(num ** 2 for num in numbers)


# print(square_sum([2, 3, 4]))


# def remove_char(s):
#     return s[1:-1]


# print(remove_char('helloy'))


# def opposite(number):
#     return -number


# print(opposite(-7))


# def summation(num):
#     return num * (num + 1)//2


# print(summation(8))

"""
str, int, float, bool, list, dict, tuple (кортеж)
"""

a = 10
b = 3.14

#    0123
s = "text"  # str
ss = 'a'  # str

bl = True

l = [1, 2, 3, 'any text']  # list
t = (1, 2, 3, 'any text')  # tuple
d = {'age': 20, 'name': 'Anna'}  # d = {key: value} # dict

print(s.upper())
print(s.find('gg'))
print(s.find('ex'))

print('a'.upper())
print('B'.lower())

# методы строк (встроенные функции в строки)

# print(dir(str))
# help(str.upper)
# help(str.split)

# Ctrl + / - закоментировать или раскомментировать


# Списки
people = [] # пустой
salary = [1000, 2000, 3000]
anything = [11, 3.14, 'Den', salary]

print(anything)
print(anything[1])
# Обзор Тестирования ПО

def func(a: int, b: str):
    return b * a


check_list = [
    [2, "text", "texttext"],
    [0, "text", ""]
]

for case_opt in check_list:
    a, b, result = case_opt
    result = func(a, b)
    print(result)

def is_year_leap(adar2):
    if adar2 % 4 == 0:
        return True
    else:
        return False


adar2 = int(input("введите год: "))

lip_year = is_year_leap(adar2)
print(f'year {adar2}: {lip_year}')

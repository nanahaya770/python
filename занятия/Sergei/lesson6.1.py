hebrew_word = input("введите слово на иврите: ")
gematria = 0
total_gematria = 0

my_dict_alef_bet_gematria = {
     'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
     'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80,
     'צ': 90, 'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400,
     'ך': 20, 'ם': 40, 'ן': 50, 'ף': 80, 'ץ': 90
}

for char in hebrew_word:
    gematria_for_char = my_dict_alef_bet_gematria.get(char)
    total_gematria = total_gematria + gematria_for_char
    print(f"гематрия буквы {char}: {gematria_for_char}")
print(f"гематрия слова {hebrew_word}: {total_gematria}")

from __future__ import print_function
import pprint as pp

columns = int(raw_input())
rows = int(raw_input())

number_of_translations = int(raw_input())

translations = {}

for _ in range(number_of_translations):
    character = raw_input()

    translation = ""
    # translation = []
    for _ in range(rows):
        translation += raw_input()
        translation += "\n"

    translations[character] = translation


# print(translations)

pp.pprint(translations)

for element in translations:
    print(translations[element])

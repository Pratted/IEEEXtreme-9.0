from __future__ import print_function

columns = int(raw_input())
rows = int(raw_input())

number_of_translations = int(raw_input())

translations = {}

for _ in number_of_translations:
    character = raw_input()

    translation = ""
    # translation = []
    for _ in rows:
        translation += raw_input() + "\n"

    translations[character] = translation


print(translations)

from __future__ import print_function

columns = int(raw_input())
rows = int(raw_input())

number_of_translations = int(raw_input())

translations = {}

for _ in range(number_of_translations):
    character = raw_input()

    translation = []
    for _ in range(rows):
        translation.append(raw_input())

    translations[character] = translation


number_of_strings = int(raw_input())

for _ in range(number_of_strings):
    output = ["" for _ in range(rows)]

    string = raw_input()

    if not string:
        print("\n" * (rows - 1))
    else:
        for character in string:
            translation = translations[character]

            for i in range(rows):
                output[i] += translation[i]

        output_string = ""
        for line in output:
            output_string += line + "\n"

        print(output_string.strip())

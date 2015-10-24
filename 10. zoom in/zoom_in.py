from __future__ import print_function
import pprint as pp

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


# print(translations)

# pp.pprint(translations)

#for element in translations:
#    print(translations[element])

number_of_strings = int(raw_input())

output = ["" for _ in range(rows)]
# print(output)

for _ in range(number_of_strings):
    string = raw_input()

    for character in string:
        translation = translations[character]

        for i in range(rows):
            output[i] += translation[i]


# print(output)

output_string = ""
for line in output:
    output_string += line + "\n"

print(output_string.strip())

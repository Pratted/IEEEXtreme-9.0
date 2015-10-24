from __future__ import print_function

number_of_test_cases = raw_input()

d_s = raw_input()
d_s = d_s.split()

# number of words in a dictionary
d = int(d_s[0])
# number of potential dictionary strings to be checked
s = int(d_s[1])

words = []
for _ in range(d):
    line = raw_input()
    words.append(line)
# print("words:")
# print(words)
# print("")

potentials = []
for _ in range(s):
    line = raw_input()
    potentials.append(line)
# print("potentials:")
# print(potentials)
# print("")

state = {}
for potentional in potentials:
    state[potentional] = ["", ""]
# print("state:")
# print(state)
# print("")

for potentional in potentials:
    print("")
    print(potentional)
    potentional = list(potentional)
    print(potentional)

    seen = {}
    for character in set(potentional):
        seen[character] = -1
    print(seen)

    print("")
    for word in words:
        print(word)

        for character in word:
            print("superlist:")
            list_dictionary = list(state)
            print(list_dictionary[seen[character]+1:])
            if character in list(state)[seen[character]+1:]:
                index = potentional.find(character)
                print("{} found in index {}".format(character, index))
                seen[character] = potentional.find(character)

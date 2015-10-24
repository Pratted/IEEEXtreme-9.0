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

potential_dictionaries = []
for _ in range(s):
    line = raw_input()
    potential_dictionaries.append(line)
# print("potential_dictionaries:")
# print(potential_dictionaries)
# print("")

state = {}
for potential_dictionary in potential_dictionaries:
    state[potential_dictionary] = ["", ""]
# print("state:")
# print(state)
# print("")

for potential_dictionary in potential_dictionaries:
    # print("")
    # print(potential_dictionary)
    potential_dictionary_list = list(potential_dictionary)
    # print(potential_dictionary_list)

    potential_dictionary_usage = {}
    for character in potential_dictionary:
        if character in potential_dictionary_usage:
            potential_dictionary_usage[character] += 1
        else:
            potential_dictionary_usage[character] = 1
    print("potential_dictionary_usage:")
    print(potential_dictionary_usage)

    original_potential_dictionary_usage = dict(potential_dictionary_usage)

    missing = 0
    for word in words:
        # print("")
        # print(word)
        word = list(word)
        # print(word)

        temp_potential_dictionary = list(potential_dictionary_list)

        temp_word = list(word)
        for character in temp_word:
            # print(character)
            if character in temp_potential_dictionary:
                word.remove(character)
                temp_potential_dictionary.remove(character)
                potential_dictionary_usage[character] += -1
            else:
                missing += 1

        for character in potential_dictionary_usage:
            if potential_dictionary_usage[character] > 0:
                potential_dictionary_usage[character] = original_potential_dictionary_usage[character]

        # print(temp_potential_dictionary)
        # print("missing: {}".format(missing))

    if not missing:
        state[potential_dictionary][0] = "Yes"
    else:
        state[potential_dictionary][0] = "No"
        state[potential_dictionary][1] = missing

    print("potential_dictionary_usage:")
    print(potential_dictionary_usage)
    print("")

    if any(potential_dictionary_usage[key] > 0 for key in potential_dictionary_usage):
        if state[potential_dictionary][0] != "No":
            state[potential_dictionary][1] = "No"
    else:
        if state[potential_dictionary][0] != "No":
            state[potential_dictionary][1] = "Yes"


print("state:")
print(state)

for potential_dictionary in potential_dictionaries:
    print(state[potential_dictionary][0] + " " + str(state[potential_dictionary][1]))

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
print("words:")
print(words)

potentional_dictionaries = []
for _ in range(s):
    line = raw_input()
    potentional_dictionaries.append(line)
print("potentional_dictionaries:")
print(potentional_dictionaries)


# for potentional_dictionary in potentional_dictionaries:

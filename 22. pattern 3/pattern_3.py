from __future__ import print_function

number_of_test_cases = int(raw_input())

test_cases = []
for _ in range(number_of_test_cases):
    line = raw_input()
    test_cases.append(line)

# print(test_cases)

def split_count(string, lenght):
    # return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]
    return [string[i:i+lenght] for i in range(0, len(string), lenght)]

for string in test_cases:
    # print("")
    # print(string)

    found = False

    pattern = string[0]
    # print(pattern)

    while not found:
        break_flag = False

        parts = split_count(string, len(pattern))
        # print(parts)

        for part in parts:
            if part not in pattern:
                pattern = string[:len(pattern) + 1]
                # print(pattern)
                break_flag = True
                break

        if break_flag:
            continue

        found = True

    print(len(pattern))

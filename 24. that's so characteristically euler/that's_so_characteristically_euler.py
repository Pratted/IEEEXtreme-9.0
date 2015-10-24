from __future__ import print_function

number_of_test_cases = int(raw_input())

for _ in range(number_of_test_cases):
    # height of the image
    n = int(raw_input())

    # width of the image
    m = int(raw_input())

    pattern = []
    for _ in range(n):
        line = raw_input()
        pattern.append(line)
    print("pattern:")
    print(pattern)
    print("")

lines = []

line = raw_input()

while line != "END":
    lines.append(line)
    line = raw_input()


# print(lines)

# results = []

for line in lines:
    # print("line: ", line)

    if line != "END":
        alphas = []

        number = int(line)
        # print(number)
        alphas.append(number)
        alphas.append(len(line))

        while alphas[-1] != alphas[-2]:
            # print(alphas)
            # print(len(alphas) - 1)
            # print

            alphas.append(len(str(alphas[-1])))

        # print(alphas)
        # print("the smallest positive i of {} is {}".format(alphas[0], alphas[-1]))
        print(len(alphas) - 1)
        # print

        # results.append(len(alphas) - 1)

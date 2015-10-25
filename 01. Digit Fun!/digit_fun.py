lines = []

line = raw_input()

while line != "END":
    lines.append(line)
    line = raw_input()


for line in lines:
    if line != "END":
        alphas = []

        number = int(line)
        alphas.append(number)
        alphas.append(len(line))

        while alphas[-1] != alphas[-2]:
            alphas.append(len(str(alphas[-1])))

        print(len(alphas) - 1)

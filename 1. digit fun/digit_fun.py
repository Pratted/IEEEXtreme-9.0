string = raw_input()

lines = string.split("\n")

def number_of_digits(number):
    """
    """
    return len(number)



for line in lines:
    if line != "END":
        number = int(line)
        alphas = []
        alphas.append(number)
        alphas.append(number_of_digits(number))
        if alphas[-1] == alphas[-2]:
            return alphas[-1]

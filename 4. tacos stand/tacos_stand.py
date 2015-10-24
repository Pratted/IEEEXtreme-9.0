days = int(raw_input())

for _ in range(days):
    shells, meat, rice, beans = raw_input().split()

    shells = int(shells)
    meat = int(meat)
    rice = int(rice)
    beans = int(beans)

    ingredients = [meat, rice, beans]
    # print(ingredients)

    ingredients.sort(reverse=True)
    # print(ingredients)

    tacos = 0

    print(ingredients)
    tacos += ingredients[1]
    tacos += min(ingredients[0] - ingredients[1], ingredients[2])

    if tacos <= shells:
        print(tacos)
    else:
        print(shells)

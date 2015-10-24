
days = int(raw_input())
ingredients = []
max_val = [0,0]
zero_count = []

for i in range(days):
    tmp.append(raw_input().split())
    zero_count.append(0)
    tacos[i] = tmp[i][0]
    for j in range(3):
        ingredients[i].append(tmp[i][j+1])
print ingredients


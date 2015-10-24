dimensions = raw_input()

rows, columns = dimensions.split(" ")
rows = int(rows)
columns = int(columns)

print("rows: ", rows)
print("columns: ", columns)

number_of_queries = int(raw_input())
print("number_of_queries: ", number_of_queries)

queries = []
for _ in range(number_of_queries):
    queries.append(raw_input())

print("queries: ", queries)

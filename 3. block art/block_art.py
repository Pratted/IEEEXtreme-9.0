from __future__ import print_function

dimensions = raw_input()

rows, columns = dimensions.split(" ")
rows = int(rows)
columns = int(columns)

# print("rows: ", rows)
# print("columns: ", columns)

number_of_queries = int(raw_input())
# print("number_of_queries: ", number_of_queries)

queries = []
for _ in range(number_of_queries):
    queries.append(raw_input())

# print("queries: ", queries)

matrix = [[0 for _ in range(columns)] for _ in range(rows)]
# print("matrix:")
# print(matrix)

for query in queries:
    elements = query.split(" ")
    operation = elements[0]
    top_left_row = int(elements[1])
    top_left_column = int(elements[2])
    bottom_right_row = int(elements[3])
    bottom_right_column = int(elements[4])

    # print("operation: ", operation)
    # print("top_left_row: ", top_left_row)
    # print("top_left_column: ", top_left_column)
    # print("bottom_right_row: ", bottom_right_row)
    # print("bottom_right_column: ", bottom_right_column)

    cubes = 0
    for row in range(top_left_row - 1, bottom_right_row):
        for column in range(top_left_column - 1, bottom_right_column):
            if operation == "a":
                matrix[row][column] += 1
            elif operation == "r":
                matrix[row][column] += -1
            elif operation == "q":
                cubes += matrix[row][column]

    if operation == "q":
        print(cubes)

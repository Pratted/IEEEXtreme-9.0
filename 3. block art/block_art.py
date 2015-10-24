from __future__ import print_function
import numpy as np

dimensions = raw_input()

rows, columns = dimensions.split(" ")
rows = int(rows)
columns = int(columns)

number_of_queries = int(raw_input())

queries = []
for _ in range(number_of_queries):
    queries.append(raw_input())

# matrix = [[0 for _ in range(columns)] for _ in range(rows)]
matrix = np.zeros((rows, columns))

for query in queries:
    # print("query: " + query)
    elements = query.split(" ")
    operation = elements[0]
    top_left_row = int(elements[1])
    top_left_column = int(elements[2])
    bottom_right_row = int(elements[3])
    bottom_right_column = int(elements[4])

    if operation == "a":
        # matrix[top_left_row-1:bottom_right_row][top_left_column-1:bottom_right_column] += 1
        matrix[top_left_row - 1:bottom_right_row, top_left_column - 1:bottom_right_column] += 1
    elif operation == "r":
        # matrix[top_left_row-1:bottom_right_row][top_left_column-1:bottom_right_column] += -1
        matrix[top_left_row - 1:bottom_right_row, top_left_column - 1:bottom_right_column] += -1
    elif operation == "q":
        #cubes = 0
        #for row in range(top_left_row - 1, bottom_right_row):
        #   for column in range(top_left_column - 1, bottom_right_column):
        #       cubes += matrix[row][column]

        cubes = sum(sum(matrix[top_left_row - 1:bottom_right_row, top_left_column - 1:bottom_right_column]))
        # sum(matrix)
        # cubes = sum(sum(matrix))
        # print(cubes)

    # print(matrix)

    if operation == "q":
        print(int(cubes))

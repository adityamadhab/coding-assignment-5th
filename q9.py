def multiply_matrices(matrix_a, matrix_b):
    result = []
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    for i in range(rows_a):
        row_result = []
        for j in range(cols_b):
            sum_product = sum(matrix_a[i][k] * matrix_b[k][j] for k in range(cols_a))
            row_result.append(sum_product)
        result.append(row_result)
    
    return result

matrix_a = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_b = [
    [7, 8],
    [9, 10],
    [11, 12]
]

result_matrix = multiply_matrices(matrix_a, matrix_b)

for row in result_matrix:
    print(row)

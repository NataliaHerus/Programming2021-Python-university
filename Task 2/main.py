def input_data(matrix):
    while True:
        try:
            matrix_size = int(input('Input an matrix size: '))
            if check_size(matrix_size) is True:
                continue
            print("Your matrix")
            for i in range(matrix_size):
                elements = []
                for j in range(matrix_size):
                    elements.append(int(input("Input a matrix element: ")))
                matrix.append(elements)
            break
        except ValueError:
            print('\nPlease try to do everything again and enter an integer number')
    return matrix_size


def check_size(matrix_size):
    if matrix_size < 2:
        print('\nSize should be bigger than 2')
        return True


def print_matrix(matrix, matrix_size):
    for i in range(matrix_size):
        for j in range(matrix_size):
            print(matrix[i][j], end=" ")
        print()


def sequence(matrix, matrix_size):
    for i in range(matrix_size):
        as_row = 0
        des_row = 0
        for j in range(matrix_size - 1):
            if matrix[i][j] > matrix[i][j + 1]:
                as_row += 1
            elif matrix[i][j] < matrix[i][j + 1]:
                des_row += 1
            elif matrix[i][j] == matrix[i][j + 1]:
                as_row += 1
                des_row += 1
        if as_row == 0:
            print("Row ", i + 1, " forms a monotonic ascending sequence\n")
        elif des_row == 0:
            print("Row ", i + 1, " forms a monotonic descending sequence\n")
        elif des_row != 0 or as_row != 0:
            print(" - ")


matrix = []
size = input_data(matrix)
print_matrix(matrix, size)
sequence(matrix, size)

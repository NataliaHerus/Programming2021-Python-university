def check_size():
    while True:
        try:
            matrix_size = int(input('Input matrix size: '))
            if matrix_size < 2:
                print('\nSize should be bigger than 2')
                continue
            break
        except ValueError:
            print("Please enter an integer positive number")
    return matrix_size


def input_number(matrix_size):
    while True:
        try:
            matrix = []
            for i in range(matrix_size):
                elements = []
                for j in range(matrix_size):
                    elements.append(int(input("Input a matrix element: ")))
                matrix.append(elements)
            break
        except ValueError:
            print("Please enter an integer number")
    return matrix


def create_matrix():
    print("Your matrix is: ")
    matrix_size = check_size()
    matrix = input_number(matrix_size)
    return matrix_size, matrix


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


def choice():
    while True:
        try:
            print("Choose what you want.\n"
                  "1 - input matrix by yourself and do options\n"
                  "2 - exit\n")
            what_chosed = int(input(""))
            if what_chosed == 1:
                matrix_size, matrix = create_matrix()
                print_matrix(matrix, matrix_size)
                sequence(matrix, matrix_size)
                continue
            elif what_chosed == 2:
                break
            else:
                print("Enter right option")
                continue
        except ValueError:
            print("Something went wrong, enter an number you want:")
            continue
        except KeyboardInterrupt:
            print("Something went wrong, enter an number you want:")
            continue
        break


choice()

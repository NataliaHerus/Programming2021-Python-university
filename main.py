def size_of_array():
    while True:
        try:
            array_size = int(input('Input an array size: '))
            if array_size <= 0:
                print('\nInteger should be bigger than 0')
                continue
            break
        except ValueError:
            print('\nPlease enter an number')
    return array_size


def input_elements(new_array, new_size):
    while True:
        try:
            for i in range(new_size):
                array_element = float(input('Input an array element: '))
                new_array.append(array_element)
            break
        except ValueError:
            print('\nPlease enter an number')
    return new_array


def minimum(full_array, whole_size):
    min_multiplication = float('inf')
    for i in range(whole_size - 1):
        if (full_array[i] * full_array[i + 1]) < min_multiplication:
            min_multiplication = full_array[i] * full_array[i + 1]
    return min_multiplication


size = size_of_array()
array = []
input_elements(array, size)
result = minimum(array, size)
print('The minimum of multiplications: ', result)

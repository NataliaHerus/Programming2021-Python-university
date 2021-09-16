def input_data(array_to_full):
    while True:
        try:
            array_size = int(input('Input an array size: '))
            if check_size(array_size) is True:
                continue
            for i in range(array_size):
                array_element = float(input('Input an array element: '))
                array_to_full.append(array_element)
                continue
            break
        except ValueError:
            print('\nPlease try to do everything again and enter an number')
    return array_size


def check_size(array_size):
    if array_size <= 1:
        print('\nSize should be bigger than 1')
        return True


def minimum(full_array, whole_size):
    min_multiplication = float('inf')
    for i in range(whole_size - 1):
        if (full_array[i] * full_array[i + 1]) < min_multiplication:
            min_multiplication = full_array[i] * full_array[i + 1]
    return min_multiplication


array = []
size = input_data(array)
result = minimum(array, size)
print('The minimum of multiplications: ', result)

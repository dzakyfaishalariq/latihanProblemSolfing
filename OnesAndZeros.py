def binary_array_to_number(arr):
    num = 0
    arr_reves = arr[::-1]
    print(arr_reves)
    for i in range(len(arr_reves)):
        num += arr_reves[i]*(2**i)
    return num

print(binary_array_to_number([1,1,1,1]))
        
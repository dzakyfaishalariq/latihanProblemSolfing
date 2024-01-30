def divisible_by(numbers, divisor):
    list_number_new = []
    for i in range(len(numbers)):
        if numbers[i] % divisor == 0:
            list_number_new.append(numbers[i])
    return list_number_new

print(divisible_by([1,2,3,4,5,6], 3))
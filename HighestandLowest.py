def high_and_low(numbers):
    num_list = numbers.split(" ")
    num_list = [int(i) for i in num_list]
    minmax = [max(num_list), min(num_list)]
    minmax = [str(i) for i in minmax]
    minmax = " ".join(minmax)
    return minmax

print(high_and_low("1 2 3 4 5"))
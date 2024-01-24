def reverse_seq(n):
    lis_arr = [a for a in range(n+1)]
    return lis_arr[n:0:-1]

print(reverse_seq(10))
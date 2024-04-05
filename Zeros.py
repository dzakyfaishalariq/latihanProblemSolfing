def no_boring_zeros(n):
    n = [x for x in str(n)]
    n = n[::-1]
    return n


print(no_boring_zeros(-3200))

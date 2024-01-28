def series_sum(n):
    if n == 0:
        return "0.00"
    sum_aritmatik = 0
    a = 1
    for i in range(n):
        sum_aritmatik += 1/a
        a += 3
    return "{:.2f}".format(sum_aritmatik)

print(series_sum(3))
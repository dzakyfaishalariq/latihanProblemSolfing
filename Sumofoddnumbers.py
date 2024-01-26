def row_sum_odd_numbers(n):
    sum_area = 0
    bil_awal = 1
    for i in range(n-1):
        for _ in range(i+1):
            bil_awal += 2
    for i in range(n):
        sum_area += bil_awal
        bil_awal += 2
    return sum_area
            

print(row_sum_odd_numbers(3))
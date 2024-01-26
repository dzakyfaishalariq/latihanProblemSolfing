def dig_pow(n, p):
    lis_tampung = []
    bantu = n
    sum_area = 0
    while bantu > 0:
        lis_tampung.append(bantu % 10)
        bantu //= 10
    lis_tampung = lis_tampung[::-1]
    for bil in lis_tampung:
        nilai = bil ** p
        p += 1
        sum_area += nilai
    if sum_area % n != 0:
        return -1
    else:
        return sum_area // n

print(dig_pow(46288,3))
def longest(a1, a2):
    uniqA1 = set(a1)
    uniqA2 = set(a2)
    uniqA1 = sorted(uniqA1)
    uniqA2 = sorted(uniqA2)
    tampung = uniqA1 + uniqA2
    tampung = sorted(set(tampung))
    return "".join(tampung)

print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))
    
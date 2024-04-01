def unique_in_order(sequence):
    list_baru = []
    i = 0
    for chr in sequence:
        if len(list_baru) == 0:
            list_baru.append(chr)
            i += 1
        elif list_baru[i-1] != chr:
            list_baru.append(chr)
            i += 1
    return list_baru


print(unique_in_order("AAAABBBCCDAABBB"))

def printer_error(s):
    true_chr = "abcdefghijklm"
    total = 0
    for chr in s:
        if chr not in true_chr:
            total += 1
    return "{}/{}".format(total, len(s))

s = str(input(">"))
print(printer_error(s))
def tow_sum(number, target):
    hasil = None
    for i in number:
        for j in number:
            if j == i:
                continue
            else:
                if i + j == target:
                    hasil = ()
                else:
                    hasil = False
    return hasil    

print(tow_sum([1,2,3], 4))
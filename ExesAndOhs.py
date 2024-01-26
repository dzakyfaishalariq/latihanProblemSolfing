def xo(s):
    s = s.lower()
    sum_x = 0
    sum_o = 0
    if "x" in s and "o" in s:
        for i in s:
            if i == "x":
                sum_x += 1
            elif i == "o":
                sum_o += 1
            else:
                continue
        if sum_x == sum_o:
            return True
        else:
            return False
    else:
        return True
    
print(xo("ooxXm"))
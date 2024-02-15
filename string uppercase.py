def is_uppercase(inp):
    str_split = inp.split(" ")
    str_join = "".join(str_split)
    if str_join.isalpha():
        if str_join.isupper():
            return True
        else:
            return False
    else:
        return True
    
print(is_uppercase("T2xwafEtigBK/3S {+LblrAc\}"))
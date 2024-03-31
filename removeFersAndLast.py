def remove_char(s):
    s_split = [t for t in s]
    s_split.pop(0)
    s_split.pop(len(s_split)-1)
    return "".join(s_split)


print(remove_char("eloquent"))

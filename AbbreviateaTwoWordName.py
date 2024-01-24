def abbrev_name(name):
    split_name = name.split(" ")
    cahr_lis = []
    for name in split_name:
        cahr_lis.append(name[0])
    cahr_lis = ".".join(cahr_lis).upper()
    return cahr_lis

print(abbrev_name("dzaky faishal"))
    
def sort_by_length(arr):
    arr_int = sorted([len(x) for x in arr])
    lis = []
    for a in arr_int:
        for i in arr:
            if a == len(i):
                lis.append(i)
            else:
                continue
    return lis


print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))

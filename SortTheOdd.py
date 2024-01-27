def sort_array(source_array):
    bantu_list = []
    index = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            bantu_list.append(source_array[i])
    bantu_list = sorted(bantu_list)
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = bantu_list[index]
            index += 1
    return source_array

print(sort_array([]))
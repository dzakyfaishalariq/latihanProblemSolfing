def descending_order(num):
    list_num = []
    num_bantu = num
    num_baru = 0
    while num_bantu != 0:
        list_num.append(num_bantu%10)
        num_bantu //= 10
    list_num = sorted(list_num,reverse=True)
    for i in range(len(list_num)):
        num_baru += list_num[i]*(10**(len(list_num)-1-i))
    return num_baru
        
print(descending_order(15))
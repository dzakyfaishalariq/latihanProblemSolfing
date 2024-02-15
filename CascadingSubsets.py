def each_cons(lst, n):
    n_bantu = 0
    bil_utama_index = 0
    tensor=[]
    vektor=[]
    while n_bantu <= lst[len(lst)-1]:
        n_bantu2 = bil_utama_index
        for i in range(n):
            vektor.append(lst[i])
            n_bantu2 += 1
            n_bantu += 1
        bil_utama_index += 1
        tensor.append(vektor)
    return tensor

print(each_cons([3, 5, 8, 13],2))
    
        
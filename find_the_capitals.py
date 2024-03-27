def capitals(word):
    h_kapital = 'ABCDEWFGHIJKLMNOPQRSTUVWXYZ'
    lis = []
    for i in range(len(word)):
        if word[i] in h_kapital:
            print(word[i])
            lis.append(i)
    return lis


print(capitals('CodEWaRs'))

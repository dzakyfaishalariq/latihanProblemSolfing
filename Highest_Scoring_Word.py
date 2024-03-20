def high(x):
    abjad = "abcdefghijklmnopqrstuvwxyz"
    dictionary_abjad = {}
    for i in range(len(abjad)):
        dictionary_abjad[abjad[i]] = i+1
    x = [tks.lower() for tks in x.split(" ")]
    lis_kata = {}
    for tks in x:
        bantu = 0
        for t in tks:
            bantu += dictionary_abjad[t]
        lis_kata[tks] = bantu
    max_abjat = ""
    for key, value in lis_kata.items():
        if max(lis_kata.values()) == value:
            max_abjat = key
        else:
            continue
    return max_abjat

if __name__ == "__main__":
    print(high("aa bbb c"))

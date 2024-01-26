def to_jaden_case(string):
    string_split = string.split(" ")
    string_split_baru = []
    for kata in string_split:
        kata_split = [ka for ka in kata]
        for i in range(len(kata_split)):
            if i == 0:
                kata_split[i] = kata_split[i].upper()
            else:
                kata_split[i] = kata_split[i].lower()
        string_split_baru.append("".join(kata_split))
    return " ".join(string_split_baru)

print(to_jaden_case("HAllo saya adalah seorang ilmuan"))
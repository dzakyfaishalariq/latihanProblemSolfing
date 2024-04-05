def title_case(title, minor_words=""):
    if title == "" and minor_words=="":
        return ""
    list_baru = [t for t in title.split(" ")]
    list_baru2 = []
    for k in list_baru:
        k = k.lower()
        if k in minor_words.lower():
            list_baru2.append(k)
        else:
            k_l = [l for l in k]
            k_l[0] = k_l[0].upper()
            list_baru2.append("".join(k_l))
    utama = [f for f in list_baru2[0]]
    utama[0] = utama[0].upper()
    list_baru2[0] = "".join(utama)
    return " ".join(list_baru2)


print(title_case('THE WIND IN THE WILLOWS', 'The In'))

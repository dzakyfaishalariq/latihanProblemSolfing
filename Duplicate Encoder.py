def duplicate_encode(word):
    word = word.lower()
    h = [hu for hu in word]
    h_baru = []
    for i in range(len(h)):
        if h.count(h[i]) > 1:
            h_baru.append(")")
        else:
            h_baru.append("(")
    return "".join(h_baru)            

print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))

def reverse_words(text):
    split_text = text.split(" ")
    kata_revers = []
    for kata in split_text:
        kata_split = [ka for ka in kata]
        kata_split = kata_split[::-1]
        kata_revers.append("".join(kata_split))
    return " ".join(kata_revers)
print(reverse_words("Hallo apa kabar kamu"))
        
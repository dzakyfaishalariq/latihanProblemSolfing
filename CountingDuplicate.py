def duplicate_count(text):
    text = text.lower()
    count_huruf = 0
    set_text = list(set(text))
    for i in set_text:
        if text.count(i) > 1 :
            count_huruf += 1
    return count_huruf

print(duplicate_count("abcdeaa"))
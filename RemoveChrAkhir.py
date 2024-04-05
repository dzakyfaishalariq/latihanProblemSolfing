def remove(s):
    if s[len(s)-1] == "!":
        return s[:len(s)-1]


print(remove("hai!!!"))

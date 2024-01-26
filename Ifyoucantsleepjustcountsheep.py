def count_sheep(n):
    string = ""
    if n == 0:
        return ""
    else:
        for i in range(n):
            string += f'{i+1} sheep...'
        return string

print(count_sheep(10))
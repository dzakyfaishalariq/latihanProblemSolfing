def draw_stairs(n):
    string = ""
    for i in range(n):
        string += "\n"
        for _ in range(i):
            string += " "
        string += "I"
    return string[1:]

print(draw_stairs(3))
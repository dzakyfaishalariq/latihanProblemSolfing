def animals(heads, legs):
    # x + y = heads
    # 2x + 4y = legs => x + 2y = legs/2
    # x = heads - y
    # heads - y + 2y = legs/2
    # heads + y = (legs/2)
    # y = (legs/2)-heads
    # x = heads - (legs/2) + heads
    # x = 2heads-(legs/2)
    if heads < 0 or legs < 0:
        return "No solutions"
    else:
        x = (2 * heads) - (legs/2)
        y = (legs/2)-heads
        if x < 0 or y < 0:
            return "No solutions"
        elif isinstance(x, int) or isinstance(y, int):
            return (x,y)
        elif isinstance(x, float) or isinstance(y, float):
            x_cek = int(x*10)%10 != 0
            y_cek = int(y*10)%10 != 0
            if x_cek or y_cek:
                return "No solutions"
            else:
                return (int(x), int(y))   
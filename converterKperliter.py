def converter(mpg):
    # mpg => kpl
    return round((mpg * 1.609344) / 4.54609188, 2)

print(converter(10))
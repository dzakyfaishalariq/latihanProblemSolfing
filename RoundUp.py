def RoundUp(n):
    n_digit = n % 10
    if n_digit == 0 or n_digit == 5:
        return (n // 10)*10
    elif n_digit >= 6 or n_digit >= -5:
        return (n // 10)*10 + 10
    elif n_digit < 5 or n_digit < -6:
        return (n // 10)*10 + 5


print(RoundUp(2))

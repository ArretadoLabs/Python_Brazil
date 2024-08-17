def max_two_numbers(x, y):
    if x > y:
        return x
    return y


def max_three_numbers(x, y, z):
    return max_two_numbers(x, max_two_numbers(y, z))

print(max_three_numbers(3,10,-10))

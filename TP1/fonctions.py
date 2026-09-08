def puissance(a, b):

    if not type(a) is int:
        raise TypeError("Only integers are allowed")
    if not type(b) is int:
        raise TypeError("Only integers are allowed")

    return a ** b


if __name__ == "__main__":

    print(puissance(2, 3))
    print(puissance(5, 0))
    print(puissance(3, 2))

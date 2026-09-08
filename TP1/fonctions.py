def puissance(a, b):

    if not type(a) is int:
        raise TypeError("Only integers are allowed")
    if not type(b) is int:
        raise TypeError("Only integers are allowed")

    if b < 0:
        raise ValueError("L'exposant doit etre positif ou nul (b < 0 est indefini ici)")

    return a ** b

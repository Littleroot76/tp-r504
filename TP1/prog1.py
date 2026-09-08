print("Hello, World!")

import fonctions as f

while True:
    a = int(input("Entrez le premier nombre (base) : "))
    b = int(input("Entrez le second nombre (exposant) : "))
    res = f.puissance(a, b)
    print(a, "puissance", b, "=", res)

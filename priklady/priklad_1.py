"""
Příklad 1: Cyklus while.

Spusť tento soubor v terminálu příkazem:
    python priklady/priklad_1.py
"""

# while opakuje blok kódu, dokud platí podmínka
pocitadlo = 0
while pocitadlo < 5:
    print("Počítadlo je:", pocitadlo)
    pocitadlo = pocitadlo + 1  # nezapomeň měnit hodnotu, jinak cyklus neskončí (nekonečný cyklus)!

print("Konec while cyklu.")

# Typický příklad použití - opakuj, dokud uživatel nezadá správnou hodnotu
heslo = ""
while heslo != "python":
    heslo = input("Zadej heslo (nápověda: python): ")

print("Správné heslo, vítej!")

# break okamžitě ukončí cyklus
cislo = 0
while True:  # "nekonečný" cyklus - ukončíme ho sami pomocí break
    cislo += 1
    if cislo > 3:
        break
    print("cislo =", cislo)

# continue přeskočí zbytek těla cyklu a pokračuje další iterací
n = 0
while n < 5:
    n += 1
    if n == 3:
        continue  # přeskočí print pro n == 3
    print("n =", n)

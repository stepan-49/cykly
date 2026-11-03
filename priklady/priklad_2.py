"""
Příklad 2: Cyklus for a funkce range().

Spusť tento soubor v terminálu příkazem:
    python priklady/priklad_2.py
"""

# range(n) vytvoří posloupnost čísel 0, 1, 2, ..., n-1
for i in range(5):
    print("i =", i)

print("---")

# range(start, stop) - od start do stop-1
for i in range(2, 6):
    print("i =", i)

print("---")

# range(start, stop, krok)
for i in range(0, 10, 2):  # sudá čísla od 0 do 8
    print("sudé číslo:", i)

print("---")

# range se dá použít i sestupně se záporným krokem
for i in range(5, 0, -1):
    print("odpočet:", i)

print("---")

# for cyklem lze procházet i řetězec - postupně po jednotlivých znacích
for znak in "Python":
    print("znak:", znak)

print("---")

# Součet čísel od 1 do 10 pomocí for cyklu
soucet = 0
for cislo in range(1, 11):
    soucet = soucet + cislo
print("Součet 1 až 10 je:", soucet)

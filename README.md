# Týden 03 – Cykly

## Cíl lekce
- Naučit se opakovat kód pomocí cyklu `while`.
- Naučit se opakovat kód pomocí cyklu `for` a funkce `range()`.
- Umět použít `break` a `continue` pro řízení průběhu cyklu.

## Výklad

### Cyklus while
Opakuje blok kódu, dokud platí podmínka:
```python
pocitadlo = 0
while pocitadlo < 5:
    print(pocitadlo)
    pocitadlo += 1  # nezapomeň měnit hodnotu, jinak vznikne nekonečný cyklus!
```

### Cyklus for a range()
```python
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):     # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (krok 2)
    print(i)
```

### break a continue
- `break` okamžitě ukončí celý cyklus.
- `continue` přeskočí zbytek aktuální iterace a pokračuje další.

Podrobné okomentované ukázky najdeš v souborech `priklady/priklad_1.py` (while) a `priklady/priklad_2.py` (for, range).

## Poznámky pro výklad (doporučený postup)

Poznámky pro učitele k vedení hodiny u jednotlivých cvičení. Bez časového rozpisu – jen doporučený postup, na co se zaměřit a časté chyby studentů.

### Úkol 1 – `soucet_do_n(n)`
- Doporučený postup výkladu: zopakuj vzor „akumulátor + cyklus" – proměnná, do které se postupně přičítá, musí být založená před cyklem s počáteční hodnotou 0. Ukaž tento vzor na jednoduchém příkladu s `for` i `while`, ať studenti vidí, že jde použít oba.
- Na co se zaměřit: krajní případ `n < 1`, který je v zadání explicitně zmíněný – jak se v takovém případě cyklus vůbec nespustí (u `range` i `while`).
- Časté chyby studentů: zapomenutá inicializace akumulátoru mimo cyklus (přepisuje se v každé iteraci); špatná horní mez `range(n)` místo `range(n + 1)`, protože `range` nezahrnuje horní hranici.
- Tip: nech studenty ručně (na papíře/tabuli) rozepsat, co se stane v jednotlivých iteracích pro malé `n`, než napíší kód.

### Úkol 2 – `pocet_sudych(n)`
- Doporučený postup výkladu: propoj s úkolem z minulé lekce (`je_sude` / modulo) a s dnešním cyklem `for` + `range` – tady se obě témata potkávají.
- Na co se zaměřit: rozdíl mezi akumulací součtu (úkol 1) a počítáním výskytů (počitadlo se zvyšuje o 1, ne o hodnotu čísla).
- Časté chyby studentů: záměna počítání sudých čísel se sečtením sudých čísel; opět chyba v horní mezi `range`.
- Tip: zeptej se, jestli lze úlohu vyřešit i bez cyklu (matematickým vzorcem) – dobrá diskuze, i když řešení cyklem je cílem cvičení.

### Úkol 3 – `faktorial(n)`
- Doporučený postup výkladu: zopakuj definici faktoriálu a zdůrazni initial hodnotu akumulátoru – na rozdíl od součtu (úkol 1) musí být počáteční hodnota u násobení `1`, ne `0`.
- Na co se zaměřit: krajní případ `faktorial(0) == 1`, který je v zadání zmíněný a snadno se na něj zapomene.
- Časté chyby studentů: počáteční hodnota akumulátoru `0` (výsledek pak vždy vyjde 0, protože cokoliv krát 0 je 0); špatný rozsah cyklu (mělo by jít od 1 do `n` včetně).
- Tip: ukaž na tabuli, proč `0` jako počáteční hodnota funguje pro sčítání, ale ne pro násobení – pěkně to ilustruje rozdíl mezi neutrálním prvkem sčítání a násobení.

## Cvičení

Doplň funkce v souborech ve složce `cviceni/`:

- **`ukol_1.py` - `soucet_do_n(n)`**: Vrať součet všech celých čísel od 1 do `n` (včetně). Pro `n < 1` vrať `0`. Pokud `n` není celé číslo (`int`), vyhoď `TypeError`.
  - Příklad: `soucet_do_n(5)` -> `15`
- **`ukol_2.py` - `pocet_sudych(n)`**: Vrať počet sudých čísel v rozsahu od 1 do `n` (včetně). Pokud `n` není celé číslo (`int`), vyhoď `TypeError`.
  - Příklad: `pocet_sudych(10)` -> `5`
- **`ukol_3.py` - `faktorial(n)`**: Vrať faktoriál čísla `n` pomocí cyklu (`faktorial(0)` je `1`). Pokud je `n` záporné, vyhoď `ValueError`.
  - Příklad: `faktorial(5)` -> `120`

## Jak si to sám zkontrolovat
```bash
pip install -r requirements.txt
pytest cviceni -v
```
Po nahrání na GitHub navíc automaticky poběží testy přes GitHub Actions – uvidíš zelenou/červenou fajfku u commitu.

## Hodnocení

Hodnocení probíhá automaticky přes GitHub Classroom:

- **Základní testy** (`test_ukol_1.py`, `test_ukol_2.py`, `test_ukol_3.py`) se spustí automaticky při každém pushi do `main` a výsledek uvidíš ihned v záložce Actions / na commitu.
- **Na jedničku** je navíc potřeba projít přísnějšími **stress testy** postavenými na knihovně [Hypothesis](https://hypothesis.readthedocs.io/), které ověřují řešení na tisících náhodných a hraničních vstupů. Tyto testy se zpřístupní až po zveřejnění oficiálního řešení vyučujícím (branch `reseni`) a poté se automaticky zahrnou do hodnocení.

## Odevzdání
Vyplň soubory v `cviceni/`, commitni a pushni do svého repozitáře do stanoveného termínu. Řešení (branch `reseni`) zveřejní vyučující až po deadline.

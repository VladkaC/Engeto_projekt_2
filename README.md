# Projekt: Bulls & Cows

## Obsah
- [1. Cíl projektu](#1-cíl-projektu)
- [2. Průběh hry](#3-průběh-hry)

---

## 1. Cíl projektu
Cílem projektu je naprogramovat **hru Bulls & Cows**, kde:
- počítač vygeneruje tajné čtyřciferné číslo s unikátními číslicemi,
- hráč hádá číslo,
- program po každém pokusu vypíše počet *bulls* (uhodnutá čísla na správném místě) a *cows* (uhodnutá čísla na špatném místě),
- hra končí, když hráč uhodne tajné číslo.

---

## 2. Průběh hry
1. Program pozdraví uživatele a vypíše úvodní text.  
2. Generuje tajné 4místné číslo:
   - všechny číslice jsou unikátní,  
   - nezačíná nulou (0 může být na jiných pozicích).  
3. Hráč opakovaně hádá číslo:
   - musí mít správnou délku,  
   - obsahovat jen číslice,  
   - nezačínat nulou,  
   - nesmí obsahovat duplicity.  
4. Pokud je vstup chybný, program vypíše zprávu a vyžádá nový tip.  
5. Program po každém pokusu vypíše počet *bulls* a *cows*.  
6. Po uhodnutí čísla se hráče zeptá, zda chce pokračovat v další hře:
   - pokud ano, program vygeneruje nové číslo a hra pokračuje,  
   - pokud ne, program ukončí hru a zobrazí:
     - celkový čas, za který uživatel uhodl všechna čísla,  
     - statistiky počtu odhadů jednotlivých her,  
     - možnost opakovat hru znovu.



#!/usr/bin/env python3
# wzięte z https://github.com/gpietrzak-pl/PythonLearning/blob/master/README.md
# Dzień 1. 27.05.2020

# losowanie
# input liczby
# sprawdzanie i wyświetlanie większa/mniejsza/równa
# (gdy trafiona to info ile było prób)

# robienie liczby losowej
import random
liczba_wylosowana_przez_komp = random.randint(1, 101)
print(liczba_wylosowana_przez_komp)

# licznik ile razy użytkownik próbował zgadnąć liczbę losową
ile_razy_zgadywal = 0

#inicjalizaja zmiennej - liczby podawanej przez ludzia
liczba_zgadywana_przez_ludzia = 102
#robienie w pętli, żeby user zgadywał i zgadywał aż zgadnie
while liczba_wylosowana_przez_komp != liczba_zgadywana_przez_ludzia:
    # branie liczby od ludzia
    # dane pobrane inputem trzeeba z-int()ować, bo dane z klawwiatury to chyba string domyślnie
    liczba_zgadywana_przez_ludzia = int(input('zgadnij jaką liczbę wylosował komputer: '))
    print(liczba_zgadywana_przez_ludzia)

    # porównywanie liczby z kompa z liczbą od ludzia

    # sprawdzanie, jak liczba podana przez ludzia ma się do liczby losowej
    if liczba_wylosowana_przez_komp > liczba_zgadywana_przez_ludzia:
        print('lecisz za nisko ze zgadywaniem')
    elif liczba_wylosowana_przez_komp < liczba_zgadywana_przez_ludzia:
        print('lecisz za wysoko ze zgadywaniem')
    # ma być robione, dopóki użytkownik nie zgadnie liczby losowej
    print(liczba_wylosowana_przez_komp == liczba_zgadywana_przez_ludzia)
    ile_razy_zgadywal += 1

print(ile_razy_zgadywal)
print('coś w ogóle zostało wykonane')

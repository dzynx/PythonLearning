# PythonLearning

Zadania:

**Dzień 1. 27.05.2020**

Program losuje liczbę z zakresu 1-100. Użytkownik podaje liczbę a program odpowiada czy liczba jest większa lub mniejsza. Jeżeli użytkownik odgadnie wylosowaną liczbę to program informuje o tym oraz podaje ilość prób jakie użytkownik podjął.

Program ma pytać o liczbę i odpowiadać, ogólnie wyglądac estetycznie.

Program musi się uruchamiac we wszystkich systemach (hashbang).

**Dzień 2. 28.05.2020**

Program prosi użytkownika o 6 liczb z zakresu 1-49. Liczby są wyświetlone poniżej w kolejności od najmniejszej do największej. Nie korzystamy z funkcji sortowania pythona, algorytm sortowania piszemy sami. Algorytm dowolny (bąbelkowe, przez wstawianie, kubełkowe, quicksort lub inne, w komentarzu info o wybranym algorytmie).

**Dzień 3. 29.05.2020**

Wykorzystaj kod z zadania z dnia 2. Podczas wprowadzania liczb użytkownik ma możliwość wprowadzić tylko liczby z podanego zakresu. Jeżeli liczba jest spoza zakresu program informuje o tym użytkownika i prosi o podanie prawidłowych liczb.

**Dzień 4. 30.05.2020**

Wykorzystaj kod z zadania z dnia 3. Po wprowadzeniu liczb program losuje 6 liczb z zakresu 1-49, liczby nie mogą się powtarzać. Program sprawdza ile liczb użytkownik prawidłowo wytypował i informuje komunikatem typu: Odgadłeś 3 liczby: x, y, z. Program ma symulować grę Lotto (Duży Lotek).

**Dzień 5. 31.05.2020**

Utwórz program konsolowy który będzie przeliczał jednostki: moc kW/KM, energię J/W, masę g/funt, temperaturę C/F.
Program po uruchomieniu ma pokazać menu:
Wybierz co chcesz przeliczyć:
1. Moc kW/KM
2. Energię J/kWh
3. Masę g/funt
4. Temperaturę C/K
0. Wyjście

Użytkownik podaję ilość (np: 1) a pod spodem jest wyświetlona informacja

1 kW = 1,36KM

1 KM = 0,74kW

i znów pojawia się poniżej menu. Program działa dopóki użytkownik nie wybierze 0 kończące program.

W programie utwórz funkcję dla każdego konwertera.

**Dzień 6. 1.06.2020**

Dzień Dziecka: wymyśl jakieś zadanie dla mnie ;)

**Dzień 7. 2.06.2020**

Przerób ostatnie zadanie tak aby funkcje nie robiły printa tylko wynik przekazywały do funkcji drukuj wynik która ma nagłówek typu def drukujWynik(float wartość1, string jednostka1, float wartość2, string jednostka2)

**Dzień 8. 3.06.2020**

Dwa zadania:
1. Given a string and a non-negative int n, return a larger string that is n copies of the original string.

string_times('Hi', 2) → 'HiHi'

string_times('Hi', 3) → 'HiHiHi'

string_times('Hi', 1) → 'Hi'

Use this function signature:
def string_times(str, n):

2. Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'

front_times('Chocolate', 3) → 'ChoChoCho'

front_times('Abc', 3) → 'AbcAbcAbc'

Use this function signature:
def front_times(str, n):

** Dzień 9. 4.06.2020 **

Napisz program który wczyta Twoje imię jako string z konsoli a następnie wykorzystując buzzer z płyty głównej wypika alfabetem morsa to imię.

** Dzień 10. 5.06.2020 **

Stwórz program, który wykorzysta programy lotto, konwerter jednostek, mors jako funkcje i pozwoli na początku wybrać z czego chcemy skorzystać. Program będzie powtarzać swoje działanie do czasu wybrania 0 z menu.

** Dzień 11. 6.06.2020 **

Użytkownik wprowadza pełne zdanie albo więcej. Program ma wyświetlić statystyki występowania poszczególnych liter w tym zdaniu np:
a: 27 razy (3,45%)
b: 4 razy (x%).... itd itd

Zdanie może być zahardcodowane w programie albo uzytkownik wprowadza z palca (może też być wczytywane z pliku) :D

** Dzień 12. 7.06.2020 **

Do zadania z dnia 11. wprowadź możliwość wczytywania zdania z pliku. Plik "slowa.txt" ma znajdować się obok pliku wynonywalnego, zaś wynik ma być wpisany do pliku wyniki.txt, w konsoli ma się pojawić tylko informacja, że zadanie zostało wykonane i wynik jest w pliku o nazwie... itd.

** Dzień 13. 8.06.2020 **

Dodaj zadanie z dni 11 i 12 do programu 10.

** Dzień 14. 9.06.2020 **

Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False

Start with:

def first_last6(nums):

** Dzień 15. 10.06.2020 **

Given an array of ints length 3, return the sum of all the elements.

sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7

Start with:
def sum3(nums):

** Dzień 16. 11.06.2020 **

Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.

make_ends([1, 2, 3]) → [1, 3]
make_ends([1, 2, 3, 4]) → [1, 4]
make_ends([7, 4, 6, 2]) → [7, 2]

Start with:

def make_ends(nums):
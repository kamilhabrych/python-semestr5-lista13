# Lista 13 - Języki programowania wysokiego poziomu


**Python (13) - Grafika, wstęp**

(1) Proszę wgrać bibliotekę graficzną graphics.py:
File/settings/project/project interpreter
Tutaj dodajemy (+) bibliotekę graphics.py. Można przeglądać bibliotekę
otwierając:
External Libraries/site-packages/graphics/
(i wreszczie plik z init)
Podstawowa składnia do stworzenia okienka, przykładowo rozmiaru 500 na
500:
from graphics import *
win = GraphWin(’NazwaOkienka’,500,500)
Na końcu można umieścić:
win.getMouse()
win.close()
Co spowoduje że po kliknięciu myszy okienko jest zamknięte.
Przetestuj zmieniając nazwę i rozmiar okienka. Dodaj po win=...:
win.setBackground(’blue’) i przetestuj (zmień też na inny kolor po angielsku).

(2) Do (1) dodamy komendy które spowodują narysowanie różnych obiektów
w okienku win. Obiekt punktowy tworzymy poleceniem:
pt=Point(x,y) gdzie x i y są współrzędnymi punktu pt.
Jego kolor można wybrać dzięki:
pt.setOutline(’red’) i wreszcie można go narysować w okienku win poprzez:
pt.draw(win).
Narysuj 3 punkty w okienku i sprawdź jak współrzędne x i y wyglądają w
okienku (np. czy y jest liczone od dołu do góry czy na odwrót).
Za pomocą pętli narysuj 1000 punktów w okienku o losowych współrzędnych. Przetestuj. Zmodyfikuj teraz tak aby kolory punktów też były losowe
z listy trzech ustalonych kolorów, np. red, blue i yellow.

(3) Poza punktami istnieje kilka innych obiektów w graphics, np. okręgi:
c=Circle(pt,prom) gdzie pt jest punktem środkowym koła o promieniu prom.
Nie jest konieczne określanie osobno pt, przykładowa poprawna składnia:
c=Cirlce(Point(100,100),50)
Aby narysować okrąg c stosujemy c.draw(win) przedtem można nadać mu
różne atrybuty, np.:
c.setOutline(’green’)
c.setWidth(10)
c.setFill(’yellow’)
Inne atrybuty możemy znaleźć przeglądając plik graphics.py.
Napisz program wyświetlający trzy okręgi, każdy innego ustalonego koloru,
i losowych punktach środkowych oraz promieniach (np. z zakersu 10-50).
Zmodyfikuj program tak aby wyświetlić 50 okręgów tak że co 1/10 sekundy
(sleep z biblioteki time) pojawia się w losowym miejscu okrąg o promieniu
z zakresu 10-30 i o losowym kolorze z jakiegoś skończonego zbioru kolorów.

(4) Przetestuj obiekty Oval i Rectangle zaglądając do graphics.py. W jednym okienku narysuj jakiś owal i prostokąt o różnych rozmiarach i kolorach.

(5) Jak w (4) przetestuj obiekt Line. Narysuj za pomocą takich obiektów
trójkąt pomiędzy punktami o współrzędnych (100,100), (200,200) i (300,150).
Zmodyfikuj tak aby narysować kolejne odcinki między 10-ma losowymi punktami i ostatni odcinek łączył 10-ty punkt z pierwszym.

(6) Za pomocą obiektów Line narysuj wielobok foremny o n bokach gdzie n
jest wprowadzane przez użytkownika za pomocą input. Wsk.: można użyć
sin i cos z biblioteki math.

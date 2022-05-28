Gra w wisielca.

Hasła do odgadnięcia przez użytkownika są w pliku miasta.txt
Z modułu random jest zaimportowana funkcja choice, której
wynikiem jest losowo wybrany element listy.
Wczytywanie haseł odbywa się za pośrednictwem funkcji 
wczytaj(nazwa) wywoływanej wewnątrz funkcji wisielec().
Wewnątrz funkcji wczytaj() jest użyta metoda strip() do
usuwania białych znaków oraz znaków końca wiersza.
Litery w pliku miasta.txt są zakodowane w utf-8, bo inaczej
nie można by było odczytywać nazw miast z polskimi 
znakami - program dla innego kodowania polskich znaków nie 
działa.

Główną funkcją programu jest funkcja wisielec() wywoływana
w programie głównym po nazwie funkcji.
W języku Python nie ma możliwości modyfikowania napisu,
trzeba więc zbudować nowy napis z jego fragmentów.

Użytkownik podaje po jednej literze i ma 10 prób odgadnięcia
hasła. W każdym momencie może spróbować odgadnąć całe hasło.
Program pokazuje ile liter ma hasło i te litery, które 
zostały już odgadnięte.

Dodatkowo została dołączona funkcja rysunek(nr) wyświetlająca
częściową szubienicę w zależności od stanu gry. Ta funkcja 
rysunkowa wykorzystuje grafikę żółwia.



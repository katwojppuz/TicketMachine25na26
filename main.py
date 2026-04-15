

# Import bibliotek
import json

# 1. Wczytaj dane z pliku prices.json i zapisz je do zmiennej jako słownik/dictionary.
with open("./prices.json", "r", encoding="UTF-8") as jf:
    prices = json.load(jf)

# 2. Utwórz pusty koszyk jako listę
cart = []

# 3. Wyświetl użytkownikowi menu główne
print("""Wybierz jedną z opcji:
1 – dodaj bilet
2 – pokaż koszyk
3 – zapłać
4 – zakończ program
""")

# 4. Pobierz jeden znak od użytkownika 
option = input("Twój wybór: ")[0]

match option:
    case "1":
        # 5.1. Wyświetl typ biletu
        print("Wybierz typ biletu:\nn – normalny\nu – ulgowy")

        # 6.1. Pobierz jeden znak od użytkownika
        ticket1 = input("Twój wybór: ")[0]

        if ticket1 == "n":
            pass
        elif ticket1 =="u":
            pass
        else:
            pass

        # 7.1. Wyświetl rodzaj biletu
        print("Wybierz typ biletu:\no – okresowy\nc – czasowy\nj – jednorazowy")
        # 8.1. Pobierz jeden znak od użytkownika
        ticket2 = input("Twój wybór: ")[0]

        if ticket2 == "o":
            pass
        elif ticket2 =="c":
            pass
        elif ticket2 =="j":
            pass
        else:
            pass

        
        # 9.1. Wyświetl dostępne opcje z pliku JSON
        # •	1 – półroczny
        # •	2 – miesięczny
        # •	3 – tygodniowy
        # •	4 – jednodniowy
        # 14.	Pobierz jeden znak.
        # 15.	Na podstawie wyboru:
        # •	odczytaj cenę z cennik
        # •	zapisz nazwę biletu
        # 16.	Dodaj bilet do listy koszyk.

        # 17.	Dodaj cenę do suma.
        # 18.	Wyświetl komunikat:
        # •	„Dodano bilet: X, cena: Y zł”
    case "2":
        pass
        # Jeśli użytkownik wybierze 2:
        # 19.	Jeśli koszyk jest pusty → pokaż komunikat.
        # 20.	W przeciwnym razie:
        # •	wypisz wszystkie bilety
        # •	pokaż sumę
    case "3":
        pass
        # Jeśli użytkownik wybierze 3:
        # 21.	Jeśli koszyk jest pusty → komunikat i powrót do menu.
        # 22.	Wyświetl:
        # •	„Do zapłaty: X zł”
        # 23.	Zapytaj o metodę płatności:
        # •	g – gotówka
        # •	k – karta
        # Jeśli g:
        # 24.	Poproś użytkownika o wpisanie kwoty (może być liczba).
        # 25.	Pobierz kwotę.
        # 26.	Jeśli kwota < suma:
        # •	komunikat „za mało pieniędzy”
        # •	wróć do wpisywania
        # 27.	Jeśli kwota ≥ suma:
        # •	oblicz resztę:
        # •	reszta = kwota - suma
        # •	wyświetl:
        # •	„Reszta: X zł”
        # Jeśli k:
        # 28.	Wyświetl komunikat:
        # •	„Płatność zaakceptowana”
        # 29.	Wyświetl:
        # •	„Dziękujemy za zakup”
        # 30.	Wyczyść:
        # •	koszyk
        # •	suma = 0
    case "4":
        pass
        # Jeśli użytkownik wybierze 4:
        # 31.	Zakończ działanie programu.
    case _:
        pass
# Import bibliotek
import json
import time

# Stałe
PROMPT = "Twój wybór: "
ERROR_MSG = "Niepoprawny wybór, spróbuj ponownie."

# 1. Wczytaj dane z pliku prices.json i zapisz je do zmiennej jako słownik/dictionary.
with open("./prices.json", "r", encoding="UTF-8") as jf:
    prices = json.load(jf)

# 2. Utwórz pusty koszyk jako listę
cart = []
end = False

while not end:
    # 3. Wyświetl użytkownikowi menu główne
    print("""Wybierz jedną z opcji:
    1 – dodaj bilet
    2 – pokaż koszyk
    3 – zapłać
    4 – zakończ program
    """)

    # 4. Pobierz jeden znak od użytkownika 
    option = input(PROMPT)[0]

    match option:
        case "1":
            ticket = {}
            # 5.1. Wyświetl typ biletu
            print("Wybierz typ biletu:\nn – normalny\nu – ulgowy")

            # 6.1. Pobierz jeden znak od użytkownika
            ticket1 = input(PROMPT)[0]

            # 7.1. Na podstawie wyboru określ rodzaj biletu i zapisz go do słownika ticket pod kluczem "discount"
            if ticket1 == "n":
                ticket["discount"] = "normalny"
            elif ticket1 =="u":
                ticket["discount"] = "ulgowy"
            else:
                print(ERROR_MSG)

            # 8.1. Wyświetl rodzaj biletu
            print("Wybierz typ biletu:\no – okresowy\nc – czasowy\nj – jednorazowy")
            # 9.1. Pobierz jeden znak od użytkownika
            ticket2 = input(PROMPT)[0]

            if ticket2 == "o":
                ticket["type"] = "okresowy"
                # 10.1.1 Wyświetl dostępne opcje z pliku JSON
                print("Wybierz okres ważnosci biletu:\n1 – półroczny\n2 – miesięczny\n3 – tygodniowy\n4 – jednodniowy")
                # 11.1.1 Pobierz jeden znak od użytkownika
                ticket3 = input(PROMPT)[0]
                match ticket3:
                    case "1": ticket["validity"] = "półroczny"
                    case "2": ticket["validity"] = "miesięczny"
                    case "3": ticket["validity"] = "tygodniowy"
                    case "4": ticket["validity"] = "jednodniowy"
                    case _: print(ERROR_MSG)

            elif ticket2 =="c":
                ticket["type"] = "czasowy"
                # 10.1.2 Wyświetl dostępne opcje z pliku JSON
                print("Wybierz okres ważnosci biletu:\n1 – 60 minut\n2 – 30 minut\n3 – 10 minut")
                # 11.1.2 Pobierz jeden znak od użytkownika
                ticket3 = input(PROMPT)[0]
                match ticket3:
                    case "1": ticket["validity"] = "60 - minutowy"
                    case "2": ticket["validity"] = "30 - minutowy"
                    case "3": ticket["validity"] = "10 - minutowy"
                    case _: print(ERROR_MSG)

            elif ticket2 =="j":
                ticket["type"] = "jednorazowy"
                # 10.1.3 Wyświetl dostępne opcje z pliku JSON
                print("Wybierz obszar ważnosci biletu:\n1 – miejski\n2 – aglomeracyjny")
                # 11.1.3 Pobierz jeden znak od użytkownika
                ticket3 = input(PROMPT)[0]
                match ticket3:
                    case "1": ticket["validity"] = "miejski"
                    case "2": ticket["validity"] = "aglomeracyjny"
                    case _: print(ERROR_MSG)
            else:
                print(ERROR_MSG)

            # 12.1	Na podstawie wyboru odczytaj cenę z cennika
            ticket["price"] = prices[ticket["discount"]][ticket["type"]][ticket["validity"]]
            # 13.1	Dodaj bilet do listy koszyk.
            cart.append(ticket)
            # 14.1	Wyświetl komunikat o dodaniu biletu do koszyka
            print(f"Dodano do koszyka bilet {ticket['discount']} {ticket['type']} {ticket['validity']} za cenę {ticket['price']}")
        case "2":
            # 5.2 Jeśli koszyk jest pusty pokaż komunikatz stosowną informacją
            if not cart:
                print("W koszykiu nie ma jeszcze żadnych biletów.")
            # 6.2 W przeciwnym razie
            else:
                # 7.2 wypisz wszystkie bilety
                print(cart)
                # 8.2 pokaż sumę
                print(f"Wartość biletów w koszyku: {sum(ticket["price"] for ticket in cart):5.2} zł.")
        case "3":
            # 5.3 Jeśli koszyk jest pusty pokaż komunikatz stosowną informacją
            if not cart:
                print("W koszykiu nie ma jeszcze żadnych biletów.")
            # 6.3 W przeciwnym razie wyświetl kwotę do zapłaty
            else:
                print(f"Do zapłaty: {sum(ticket["price"] for ticket in cart):5.2} zł.")
            # 7.3 Zapytaj o metodę płatności:
            print("Wybierz metodę płatnoścu:\nk – karta\ng – gotówka\nb - blik")
            # 8.3 Pobierz jeden znak od użytkownika
            payment_method = input(PROMPT)[0]
            match payment_method:
                case "k": input("Proszę zbliżyć kartę ...")
                case "b": 
                    blik = input("Podaj kod BLIK: ")
                    if len(blik) != 6: 
                        print("Płatność nie powiodła się, spróbuj ponownie")
                case "g": 
                    to_pay = sum(ticket["price"] for ticket in cart)
                    paid = 0
                    while paid < to_pay:
                        # 9.3.3 Poproś użytkownika o wpisanie kwoty.
                        paid += float(input("Wrzuć pieniądze: "))
                        # 10.3.3	Jeśli kwota > suma:
                        if paid > to_pay:
                            #11.3.3 oblicz i wyświetl resztę
                            print(f"Reszta: {(paid - to_pay):5.2} zł.")
                case _: 
                    print(ERROR_MSG)
            # 12.3 "Wydrukuj bilety i Wyświetl komunikat „Dziękujemy za zakup”
            print("Drukowanie biletów ...")
            time.sleep(len(cart))
            print("Dziękujemy za skorzystanie z automatu biletowego. Zapraszamy ponownie!")
            # 13.3 Wyczyść koszyk
            cart = []
            # 14.3 Zakończ działanie programu.
            end = True
        case "4":
            choice = input("Czy na pewno chcesz porzucić koszyk?\nt - tak\nn - nie: ")[0]
            if choice == "t":
                # 5.4 Zakończ działanie programu.
                end = True
            if choice == "n":
                continue
            else: print(ERROR_MSG)
        case _:
            print(ERROR_MSG)
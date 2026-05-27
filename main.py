# Import bibliotek
import json
import time

# Stałe
PROMPT = "Twój wybór: "
ERROR_MSG = "Niepoprawny wybór, spróbuj ponownie."

# Funkcje
def display_menu(cart, prices):
    # 3. Wyświetl użytkownikowi menu główne
    print()
    print("Wybierz jedną z opcji:\n1 – dodaj bilet\n2 – pokaż koszyk\n3 – zapłać\n4 – zakończ program")

    # 4. Pobierz jeden znak od użytkownika 
    option = input(PROMPT)[0]

    match option:
        case "1":
            add_ticket(cart, prices)
        case "2":
            display_cart(cart)
        case "3":
            register_payment(cart, prices)
        case "4":
            end_machine(cart, prices)
        case _:
            print(ERROR_MSG)

def display_cart(cart):
    # 5.2 Jeśli koszyk jest pusty pokaż komunikat z stosowną informacją
    if not cart:
        print("W koszykiu nie ma jeszcze żadnych biletów.")
    # 6.2 W przeciwnym razie
    else:
        # 7.2 wypisz wszystkie bilety
        print("Zawartość koszyka")
        print()
        print("Lp. |    Cena    | Bilet")
        for index, ticket in enumerate(cart):
            print(f"{index+1:3} | {ticket['price']:7.2f} zł | Bilet {ticket['discount']} {ticket['type']} {ticket['validity']}")
        print()
        # 8.2 pokaż sumę
        print(get_cart_value(cart))

def register_payment(cart, prices):
    # 5.3 Jeśli koszyk jest pusty pokaż komunikat z stosowną informacją
    if not cart:
        print("W koszykiu nie ma jeszcze żadnych biletów.")
    # 6.3 W przeciwnym razie wyświetl kwotę do zapłaty
    else:
        print(get_cart_value(cart))
        # 7.3 Zapytaj o metodę płatności:
        while True:
            print("Wybierz metodę płatnoścu:\nc – karta\ng – gotówka\nb - blik\np - powrót\nk - koniec")
            # 8.3 Pobierz jeden znak od użytkownika
            payment_method = input(PROMPT)[0]
            match payment_method:
                case "c": 
                    pay_by_card()
                    break
                case "b": 
                    pay_by_blik(cart, prices)
                    break
                case "g": 
                    pay_by_cash(cart)
                    break
                case "p":
                    display_menu(cart, prices)
                case "k":
                    end_machine(cart, prices)
                case _: 
                    print(ERROR_MSG)
   
    # 12.3 "Wydrukuj bilety i Wyświetl komunikat „Dziękujemy za zakup”
    print("Drukowanie biletów ...")
    time.sleep(len(cart))
    print("Dziękujemy za skorzystanie z automatu biletowego. Zapraszamy ponownie!")
    # 13.3 Wyczyść koszyk
    cart.clear()
    # 14.3 Zakończ działanie programu.
    exit()

def pay_by_card():
    input("Proszę zbliżyć kartę ...")

def pay_by_cash(cart):
    to_pay = sum(ticket["price"] for ticket in cart)
    paid = 0
    while paid < to_pay:
        print(f"Kwota do zapłaty: {(to_pay - paid):5.2} zł.")
        # 9.3.3 Poproś użytkownika o wpisanie kwoty.
        paid += float(input("Wrzuć pieniądze: "))
        # 10.3.3	Jeśli kwota > suma:
        if paid > to_pay:
            #11.3.3 oblicz i wyświetl resztę
            print(f"Reszta: {(paid - to_pay):5.2} zł.")

def pay_by_blik(cart, prices):
    blik = input("Podaj kod BLIK: ")
    if len(blik) != 6 or not blik.isdigit(): 
        print("Płatność nie powiodła się, spróbuj ponownie")
        register_payment(cart, prices)

def get_cart_value(cart):
    return f"Wartość biletów w koszyku: {sum(ticket['price'] for ticket in cart):5.2f} zł."

def end_machine(cart, prices):
    choice = input("Czy na pewno chcesz porzucić koszyk (t - tak)? ")[0]
    if choice == "t":
        # 5.4 Zakończ działanie programu.
        exit()
    else: display_menu(cart, prices)

def add_ticket(cart, prices):
    ticket = {}

    def choose_discount():
        while True:
            # 5.1. Wyświetl typ biletu
            print("Wybierz typ biletu:\nn – normalny\nu – ulgowy\np - powrót\nk - koniec")
            # 6.1. Pobierz jeden znak od użytkownika
            ch = input(PROMPT)[0]
            if ch == "n":
                ticket["discount"] = "normalny"
                return
            elif ch == "u":
                ticket["discount"] = "ulgowy"
                return
            elif ch == "p":
                display_menu(cart, prices)
                return
            elif ch == "k":
                end_machine(cart, prices)
            else:
                print(ERROR_MSG)

    def choose_validity_from_map(prompt_text, options_map):
        while True:
            print(prompt_text)
            ch = input(PROMPT)[0]
            if ch in options_map:
                ticket["validity"] = options_map[ch]
                return
            elif ch == "p":
                display_menu(cart, prices)
                return
            elif ch == "k":
                end_machine(cart, prices)
            else:
                print(ERROR_MSG)

    def choose_type():
        while True:
            # 8.1. Wyświetl rodzaj biletu
            print("Wybierz typ biletu:\no – okresowy\nc – czasowy\nj – jednorazowy\np - powrót\nk - koniec")
            ch = input(PROMPT)[0]

            if ch == "o":
                ticket["type"] = "okresowy"
                choose_validity_from_map(
                    "Wybierz okres ważnosci biletu:\n1 – półroczny\n2 – miesięczny\n3 – tygodniowy\n4 – jednodniowy\np - powrót\nk - koniec",
                    {"1": "półroczny", "2": "miesięczny", "3": "tygodniowy", "4": "jednodniowy"},
                )
                return

            elif ch == "c":
                ticket["type"] = "czasowy"
                choose_validity_from_map(
                    "Wybierz okres ważnosci biletu:\n1 – 60 minut\n2 – 30 minut\n3 – 10 minut\np - powrót\nk - koniec",
                    {"1": "60 - minutowy", "2": "30 - minutowy", "3": "10 - minutowy"},
                )
                return

            elif ch == "j":
                ticket["type"] = "jednorazowy"
                choose_validity_from_map(
                    "Wybierz obszar ważnosci biletu:\n1 – miejski\n2 – aglomeracyjny\np - powrót\nk - koniec",
                    {"1": "miejski", "2": "aglomeracyjny"},
                )
                return

            elif ch == "p":
                display_menu(cart, prices)
                return
            elif ch == "k":
                end_machine(cart, prices)
            else:
                print(ERROR_MSG)

    choose_discount()
    choose_type()

    # 12.1	Na podstawie wyboru odczytaj cenę z cennika
    ticket["price"] = prices[ticket["discount"]][ticket["type"]][ticket["validity"]]
    # 13.1	Dodaj bilet do listy koszyk.
    cart.append(ticket)
    # 14.1	Wyświetl komunikat o dodaniu biletu do koszyka
    print(f"Dodano do koszyka bilet {ticket['discount']} {ticket['type']} {ticket['validity']} za cenę {ticket['price']}")

def main():
    # 1. Wczytaj dane z pliku prices.json i zapisz je do zmiennej jako słownik/dictionary.
    with open("./prices.json", "r", encoding="UTF-8") as jf:
        prices = json.load(jf)

    # 2. Utwórz pusty koszyk jako listę
    cart = []

    while True:
        display_menu(cart, prices)

    
import logging
import sys
logging.basicConfig(level=logging.DEBUG)

operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
 
def calculator(first_number,second_number):
    if operation == 1:
        adding = first_number + second_number
        logging.info(f"Dodaję liczby {first_number} i {second_number}")
        print(f"Wynik to {adding}")
    elif operation == 2:
        subtraction = first_number - second_number
        logging.info(f"Odejmuje {first_number} i {second_number}")
        print(f"Wynik to {subtraction}")
    elif operation == 3:
        multiplication = first_number * second_number
        logging.info(f"Mnoże liczby {first_number} i {second_number}")
        print(f"Wynik to {multiplication}")
    elif operation == 4:
        division = first_number / second_number
        logging.info(f"Dziele {first_number} przez {second_number}")
        print(f"Wynik to {division}")



calculator(int(input("Podaj pierwsza liczbę:")),int(input("Podaj druga liczbę:")))

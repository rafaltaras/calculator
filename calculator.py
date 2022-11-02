import logging
import sys
logging.basicConfig(level=logging.DEBUG)

print("Podaj działanie, posługując się odpowiednią liczbą:")
print("1 Add")
print("2 Subtract")
print("3 Multiply")
print("4 Divide")
operation = int(input("Jakie chcesz działanie 1/2/3/4: "))


lista = []
liczba = int(input("Podaj 1st liczbe: "))
lista.append(liczba)
liczba = int(input("Podaj 2st liczbe: "))



     

# Deklaracja funkcji
def add(lista):
    add = sum(lista)
    logging.info(f"Dodaję liczby {lista}")
    print(f"Wynik to {add}")

def minus(lista):
    minus = lista[0] - lista[1]
    logging.info(f"Odejmuje liczby {lista}")
    print(f"Wynik to {minus}")

def multiplication(lista):
    wynik = 1
    for liczba in lista:
        wynik = liczba * wynik
    logging.info(f"Mnożę liczby {lista}")
    print(f"Wynik to {wynik}")

def division(lista):
    result = lista[0] / lista[1]
    logging.info(f"Dzielenie liczby {lista[0]} przez {lista[1]}")
    print(f"Wynik to {result}")


# Wybór działania
if operation == 1:
    while True: 
        lista.append(liczba)
        liczba = int(input("Podaj kolejna liczbe, albo wciśnij 0 (zero) aby wykonac działanie: "))
        if liczba == 0:
            break
    add(lista)

if operation == 2:
    lista.append(liczba)
    minus(lista)

if operation == 3:
    while True: 
        lista.append(liczba)
        liczba = int(input("Podaj kolejna liczbe, albo wciśnij 0 (zero) aby wykonac działanie: "))
        if liczba == 0:
            break
    multiplication(lista)

if operation == 4:
    lista.append(liczba)
    division(lista)

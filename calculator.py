import logging
logging.basicConfig(level=logging.DEBUG)

print("Podaj działanie, posługując się odpowiednią liczbą:")
print("1 Add")
print("2 Subtract")
print("3 Multiply")
print("4 Divide")
operation = int(input("Jakie chcesz działanie 1/2/3/4: "))


lista = []
liczba = float(input("Podaj 1st liczbe: "))
lista.append(liczba)
liczba = float(input("Podaj 2st liczbe: "))
  

# Deklaracja funkcji
def add(lista):
    suma = sum(lista)
    return suma
    
def minus(lista):
    subtraction = lista[0] - lista[1]
    return subtraction

def multiplication(lista):
    wynik = 1
    for liczba in lista:
        wynik = liczba * wynik
    return wynik

def division(lista):
    result = lista[0] / lista[1]
    return result


# Wybór działania
if operation == 1:
    while True: 
        lista.append(liczba)
        liczba = float(input("Podaj kolejna liczbe, albo wciśnij 0 (zero) aby wykonac działanie: "))
        if liczba == 0:
            break
    logging.info(f"Dodaję liczby {lista}")
    suma = add(lista)
    print(f"Wynik to {suma}")


if operation == 2:
    lista.append(liczba)
    logging.info(f"Odejmuje od liczby {lista[0]} liczbę {lista[1]}" )
    subtraction = minus(lista)
    print(f"Wynik to {subtraction}")

if operation == 3:
    while True: 
        lista.append(liczba)
        liczba = float(input("Podaj kolejna liczbe, albo wciśnij 0 (zero) aby wykonac działanie: "))
        if liczba == 0:
            break
    logging.info(f"Mnożę liczby {lista}")
    wynik = multiplication(lista)
    print(f"Wynik to {wynik}")

if operation == 4:
    lista.append(liczba)   
    logging.info(f"Dzielenie liczby {lista[0]} przez {lista[1]}")
    result = division(lista)
    print(f"Wynik to {result}")

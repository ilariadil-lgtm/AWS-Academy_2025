# per vedere il reference count usiamo sys.getrefcount()
# il reference count indica quante variabili puntano allo stesso oggetto
# nota: getrefcount() restituisce sempre +1 perché crea un riferimento temporaneo

import sys

a: int = 320

b = a
print(f"refcount(a) = {sys.getrefcount(a)}")

# per vedere l'indirizzo di un oggetto usiamo il metodo id()
# può essere usato per identificare l'indirizzo referenziato da una variabile (tag) - id(a)
# può essere usato per identificare l'indirizzo dell'oggetto stesso - id(20)

a: int = 320
print(f"id(a) = {id(a)}")  # stampa l'indirizzo di memoria dell'oggetto 20

b: int = a
print(f"id(b) = {id(b)}") # stampa l'indirizzo di memoria dell'oggetto 20

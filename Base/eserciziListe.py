# Creazione di una lista di prezzi
lista_prezzi = [5, 25, 10, 40, 34, 66, 100, 53, 52, 88, 99, 102, 77, 365, 1030, 2, 44, 12, 62, 35, 74, 21, 11]
print(lista_prezzi)


#Lunghezza della lista
print(f"La lista contiene {len(lista_prezzi)} elementi.")


lista_prezzi[11] = 2654
print(lista_prezzi)

print("===========================================\n\n")

articoli = []
# Aggiungi alla lista articoli

for i in range(5):
    if i == 0:
        articoli.append(input("Inserisci il primo articolo: "))
    else:
        articoli.append(input("Inserisci un altro articolo: "))

# stampa la lista articoli
print("Lista degli articoli\n")
for articolo in articoli:
    print(f"Articolo: {articolo}")

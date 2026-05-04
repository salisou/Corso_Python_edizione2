studenti = {}

nome = input("Inserisci il nome dello studente: ")
voti_input = int(input("Inserisci il voto dello studente es: (8, 52, 33,55...): "))

voti = voti_input.split(",") # Esempio la split serve per dividere una stringa in una lista di stringhe, utilizzando un delimitatore specificato (in questo caso la virgola).
voti = [int(v) for v in voti]

studenti[nome] = voti

for nome, voti in studenti.items():
    print(f"Studente: {nome} - Voti: {voti}")

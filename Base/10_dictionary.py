# I dictionary (dizionario) è una struttura che salva dati in coppie chiave-valore.

# Creazione di un dizionario
persona = {
    "nome": "Luca", # chiave: nome, valore: Luca
    "cognome": "Salvato", # chiave: cognome, valore: Salvato
    "età": 30, # chiave: età, valore: 30
    "città": "Roma", # chiave: città, valore: Roma
    "codice_fiscale": "LCCLCA80A01H501U", # chiave: codice_fiscale, valore: LCCLCA80A01H501U
    "professione": "Ingegnere" # chiave: professione, valore: Ingegnere
}

# Accedere ai   valori del dizionario
print(persona["nome"]) # Output: Luca   

# Più sicuro è usare il metodo get() che restituisce None se la chiave non esiste, invece di generare un errore
print(persona.get("codice_fiscale")) # Output: LCCLCA80A01H501U

# Modificare un valore esistente
persona["cognome"] = "Rossi"
print(persona["cognome"]) # Output: Rossi

#Aggiungere una nuova coppia chiave-valore
persona["professione"] = "Ingegnere"

print("\n================================================\n")

# Ciclo for per stampare tutte le chiavi 
print("Chiavi del dizionario:")
for key in persona:
    print(f"Chiave: {key}")
    
# Ciclo for per stampare tutti i valori
print("\nValori del dizionario:")
for value in persona.values():
    print(f"Valore: {value}")
    
# Ciclo for per stampare tutte le coppie chiave-valore
print("\nCoppie chiave-valore del dizionario:")
for chiave, valore in persona.items():
    print(f"Chiave: {chiave} - Valore: {valore}")

# Esempio reale (Registro studenti)
studenti = {
    "mario" : 36,
    "luca" : 30,
    "simona" : 28,
    "andrea" : 25,
    "melania" : 29,
    "catalina" : 27,
    "giovanni" : 31,
    "giseppe" : 26,
    "mattia": 32,
    "francesca" : 24
}

# Calcolare la media dei voti degli studenti
media = sum(studenti.values()) / len(studenti)


# Calcolare il voto massimo e minimo
massimo_voto = max(studenti.values())
minimo_voto = min(studenti.values())


print(f"La media dei voti è: {media:.2f}")
print(f"Il valore massimo è {massimo_voto}")
print(f"Il valore minimo è {minimo_voto}")

print("\n================================================\n")
# Lista degli studenti (sopra/sotto) la media
print("Studenti sopra la media:")

for nome, voto in studenti.items():
    if voto >= media:
        print(f"I nomi degli studenti sopra la media sono: {nome}.")
    else:
        print(f"I nomi degli studenti sotto la media sono: {nome}.")




print("Fine Studenti sopra la media:")

for nome, voto in studenti.items():
    print(f"Nome : {nome} - Voto: {voto}")
    
# Voto media degli studenti

    
# Esempio 2: Dizionario con lista di voti
studenti_voti = {}

studenti["luana"] = [28, 30, 27]
studenti["Brenda"]= [27, 28, 30, 27, 28]
studenti["melania"]= [25, 29, 30, 24, 27, 30, 24]



for studente, voto in studenti.items():
    print(f"Studente : {studente.upper()} ha un voto di: {voto}")
    
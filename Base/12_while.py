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

studenti["simona"]


nomi = list(studenti.keys())
# voti = list(studenti.values())

i = 0

# while -> ciclo che si ripete finché una condizione è vera
while i < len(nomi): 
    nome = nomi[i]
    voto = studenti[nome]
    print(f"Studente: {nome} - Voto: {voto}")
    i += 1
    
"""
    Il While lavora con indici (0,1,2,3..), mentre il dizionario no.
    Quindi trasforma la chiave in lista
    
    Esempio: 
        list(studenti.keys())
"""
# titolo: "Siamo alla Frutta!"
# studente: Salomon

class Frutto:
    def __init__(self, nome, colore, prezzo):
        self.nome = nome
        self.colore = colore
        self.prezzo = prezzo
    
    def descrizione(self):
        return f"{self.nome} è di colore {self.colore} e costa {self.prezzo:.2f} euro."
    
    def __str__(self):
        return f"{self.nome} è di colore {self.colore} e costa {self.prezzo:.2f} euro."


class Mela(Frutto):
    def __init__(self, nome, colore, prezzo, varietà):
        super().__init__(nome, colore, prezzo)
        self.varietà = varietà
    
    def descrizione(self):
        return f"{self.nome} è una mela {self.varietà}, di colore {self.colore}, e costa {self.prezzo:.2f} euro."


class Banana(Frutto):
    def __init__(self, nome, colore, prezzo, maturazione):
        super().__init__(nome, colore, prezzo)
        self.maturazione = maturazione

    def descrizione(self):
        return f"{self.nome} è una banana {self.maturazione}, di colore {self.colore}, e costa {self.prezzo:.2f} euro."

class Arancia(Frutto):
    def __init__(self, nome, colore, prezzo):
        super().__init__(nome, colore, prezzo)
    
    def descrizione(self):
        tipo = "da spremuta"
        return f"{self.nome} è un'arancia {tipo}, di colore {self.colore}, e costa {self.prezzo:.2f} euro."

mela = Mela("Questa mela", "rosso", 1.20, "Golden")
banana = Banana("Questa banana", "giallo", 0.80, "matura")
pera = Frutto("Questa pera", "verde", 1.10)     # qui non ho creato una sottoclasse, ma ho usato direttamente "Frutto"
arancia = Arancia("Questa arancia", "arancione", 0.50)

frutti = [mela, banana, pera, arancia]

for frutto in frutti:
    print(frutto)
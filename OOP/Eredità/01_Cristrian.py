# CLASSE Alimenti (Classe GENITORE)
class Alimenti:
    def __init__(self, id_prodotto, categoria):
        self._id_prodotto = id_prodotto
        self._categoria = categoria

    def info(self):
        return f"{self._id_prodotto} {self._categoria}"

    def Avvia(self):
        return "Questo prodotto proviene da ..."

# CLASSE DEI PRODOTTI (Classe Genitore: Alimenti -> Classe Figlio: Prodotto)
class Prodotto(Alimenti):
    def __init__(self, id_prodotto, categoria, nome_prodotto, provenienza):
        super().__init__(id_prodotto, categoria)
        self._nome_prodotto = nome_prodotto
        self._provenienza = provenienza
    
    def Aggiungere(self):
        return f"{self._nome_prodotto} {self._provenienza}"

    def Avvia(self):
        return f"Questo prodotto ha le seguenti informazioni \n|{self.info()} {self.Aggiungere()}|\n"

# CLASSE DELLE CONSERVE (Classe Genitore: Prodotto -> Classe Figlio: Conserva)
class Conserva(Prodotto):
    def __init__(self, id_prodotto, categoria, nome_prodotto, provenienza):
        super().__init__(id_prodotto, categoria, nome_prodotto, provenienza)
        self._nome_prodotto = nome_prodotto
        self._provenienza = provenienza
    
    def Aggiungere(self):
        return f"{self._nome_prodotto} {self._provenienza}"
    
    def Avvia(self):
        return f"Queste conserve etichettate \n|{self.info()} {self.Aggiungere()}| sono ECCELLENTI\n"
    

# AVVIO DEL PROGRAMMA
prodotto = Prodotto("ID: 001 -", "CATEGORIA: Frutta -", "DENOMINAZIONE: Mela -", "PROVENIENZA: Trentino Alto-Adige")
conserva = Conserva("ID: 005 -", "CATEGORIA: Verdura -", "DENOMINAZIONE: Melenzana -", "PROVENIENZA: Campania")

print(prodotto.Avvia())

print(conserva.Avvia())
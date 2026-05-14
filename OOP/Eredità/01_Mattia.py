class Libro:
    def __init__(self, titolo, autore, anno_pubblicazione):
        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione

    def descrizione(self):
        return f"{self.titolo} di {self.autore}; libro pubblicato nel {self.anno_pubblicazione}."

    def Pubblicato(self):
        return "Il libro è stato pubblicato."

class I_Cariolanti(Libro):
    def __init__(self, titolo, autore, anno_pubblicazione, genere):
        super().__init__(titolo, autore, anno_pubblicazione)
        self.genere = genere
    
    def Pubblicato(self):
        return f"{self.titolo} è un libro del genere {self.genere} ed è stato pubblicato nel {self.anno_pubblicazione}."

class La_Nonna_Sul_Melo(Libro):
    def __init__(self, titolo, autore, anno_pubblicazione, ambientazione):
        super().__init__(titolo, autore, anno_pubblicazione)
        self.ambientazione = ambientazione
    
    def Pubblicato(self):
        return f"{self.titolo} è un ambientato in {self.ambientazione} ed è stato pubblicato nel {self.anno_pubblicazione}."


Libro1 = I_Cariolanti("I Cariolanti", "Sacha Naspini", 2009, "Narrativa")
Libro2 = La_Nonna_Sul_Melo("La Nonna sul Melo", "Mira Lobe", 1965, "un giardino magico")

print(Libro1.descrizione())
print(Libro1.Pubblicato())

print(Libro2.descrizione())
print(Libro2.Pubblicato())
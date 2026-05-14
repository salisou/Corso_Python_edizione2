class Libro:
    def __init__(self,titolo, pagine):
        self._titolo = titolo
        self._pagine = pagine
        

    def info(self):
        return f"{self._titolo} {self._pagine}"

    def vendi(self):
        return f"{self._titolo} ha venduto 100mila copie!"
    
    def leggi(self):
        return f"Hai letto tutte le {self._pagine} pagine di {self._titolo}"
    

class Atlante(Libro):
    def __init__(self, titolo, pagine, immagini):
        super().__init__(titolo, pagine)
        self._immagini = immagini

    def consulta(self):
        return f"Hai consultato {self._titolo}"

    def vendi(self):
        return f"Hai rivenduto {self._titolo}"

class Dizionario(Atlante):
    def __init__(self, titolo, pagine, immagini, editore):
        super().__init__(titolo, pagine, immagini)
        self._editore = editore

    def consulta(self):
        return f"Sei riuscito a trovare la parola che cercavi in {self._editore}? Spero di sì"


libro = Libro("Il caso Hanry Quebert", 650)

atlante = Atlante("Encarta", 1250, 250)

dizionario = Dizionario("Treccani", 1500, 650, "Treccani e Gentile")

print(libro.info())
print(libro.leggi())
print(libro.vendi())

print(dizionario.info())
print(dizionario.consulta())
print(dizionario.vendi())

print(atlante.info())
print(atlante.consulta())
print(atlante.vendi())




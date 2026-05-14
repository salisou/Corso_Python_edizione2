# Dichiarazione del Metodo con (def)
# Dichiarazione dell'atributo con (self)
# Dichiarazione del construttore della classe con def __init__(self):

class Persona:
    def __init__(self, nome, cognome):
        self._nome = nome
        self._cognome = cognome

    def info(self):
        return f"{self._nome} {self._cognome}"

class Studente(Persona):
    def __init__(self, nome, cognome, tipo_studente):
        super().__init__(nome, cognome)
        self._tipo_studente = tipo_studente

    def Risultato(self):
            return f"{self.info()} è uno {self._tipo_studente}. "

class Lavoratore(Persona):
    def __init__(self, nome, cognome, tipo_lavoratore):
        super().__init__(nome, cognome)
        self._tipo_lavoratore = tipo_lavoratore

    def Risultato(self):
            return f"{self.info()} è un {self._tipo_lavoratore}. "

studente = Studente("Antonio", "Bambino", "studente di giurisprudenza")

lavoratore = Lavoratore("Pinco", "Pallino", "consulente del lavoro")

print(studente.info())
print(studente.Risultato())

print(lavoratore.info())
print(lavoratore.Risultato())
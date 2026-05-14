class Persona:
    def __init__(self, nome, cognome):
        self._nome = nome
        self._cognome = cognome
    
    def Saluta(self):
        print("Caio sono " + self._nome)

class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self._materia = materia
    
    def Saluta(self):
        print("Buongiorno sono " + self._nome + " " + self._cognome + " insegno la " + self._materia)
    
    def Voto(self):
        print("Bravo, hai un bel 8")


persona1 = Persona("Filippo", "Battaglia")  
persona2 = Insegnante("Filippo", "Battaglia", "Matematica")

persona1.Saluta()
persona2.Saluta()
persona2.Voto()

print(persona1.Saluta())
print(persona2.Saluta())
print(persona2.Voto())  
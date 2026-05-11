class Studenti:
    # costruttore vuoto
    # def __init__(self): # public Persona(){}
    #     pass
    
    # metodo con parametri  public Persona(.........){}
    def __init__(self, nome="", cognome="", email="", telefono=""):
        # Atributi (propietà) del costruttore della calsse
        self._nome     = nome 
        self._cognome  = cognome
        self._email    = email
        self._telefono = telefono
    
    # inserisci_dati():
    
    def Inserisci_dati(self):
        self._nome = input("Inserisci tuo nome: ")
        self._cognome = input("Inserisci tuo cognome: ")
        self._email = input("Inserisci tua mail: ")
        self._telefono = input("Inserisci il nume di telefono: ")
        
    def __str__(self):
        return f"{self._nome} {self._cognome} {self._email} {self._telefono}"
    
    def Salute(self):
        print("Ciao mi chiamo ")

class Sampa:
    def __init__(self):
        # nome = input("Inserisci tuo nome: ")
        # cognome = input("Inserisci tuo cognome: ")
        # email = input("Inserisci tua mail: ")
        # telefono = input("Inserisci il nume di telefono: ")
    
        # studente = Studenti(nome, cognome, email, telefono)
        studente = Studenti()
        # studente.Inserisci_dati()
        studente.Salute()

        print(f"Registro Studenti: {studente}")
Sampa()


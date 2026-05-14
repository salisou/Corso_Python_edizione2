class Telefono:
    def __init__(self, marca):
        self._marca = marca

    def chiama(self, numero, marca):
        return f"Chiamando il numero {numero} di un {marca}.. "
    
class Smartphone(Telefono):
    def __init__(self, marca, modello):
        super().__init__(marca)
        self._modello = modello

    def invia_email(self, email, messaggio):
        return f"Enviando email a {email} dal mio {self._modello}. Mensaggio: {messaggio}."   

mio_cel = Smartphone("Apple", "Iphone 16") 

print(mio_cel.chiama("123456123", "Iphone"))  

print(mio_cel.invia_email("bren@scuola.it", "Hola profe, ¡funciona la herencia!"))  
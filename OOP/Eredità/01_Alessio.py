class Bar:
    def __init__(self,Quantita,Vol):
        self._Quantita = Quantita
        self._Vol =Vol

    def info (self):
        return f"{self._Quantita} {self._Vol}"

    def Avvia(self):
        return f"{self.info()} presenti a bar"

class Gin(Bar):
    def __init__(self,Quantita,Vol,Marca):
        super().__init__(Quantita,Vol)
        self._Marca = Marca

    def info(self):
        return f"{self._Quantita} {self._Vol} {self._Marca}"
    
    def Avvia (self): 
        return f"[{self.info()}] sono nel magazzino"
    
class Vino(Bar):
        def __init__ (self,Quantita,Vol,Vitigno):
            super().__init__(Quantita,Vol)
            self._Vitigno = Vitigno
        def info(self):
            return f"{self._Quantita} {self._Vol} {self._Vitigno}"
        def Avvia(self):
            return f"[{self.info()}] sono nel Magazzino"

        
Gin1 = Gin(1, 40, "Beefeater")
Vino1 = Vino(2, 13, "Pinot Grigio")
Gin2 = Gin(23, 38, "Bombay")
Vino2 = Vino(5, 14, "Sangiovese")

print(Gin1.Avvia())
print(Vino1.Avvia())
print(Gin2.Avvia())
print(Vino2.Avvia())
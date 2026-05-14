
class Libreria:
    def __init__(self, editore, autore):
        self ._editore = editore
        self._autore = autore

    def Info(self):
        return f"{self._editore} {self._autore}"  

    def Avvia(self):
        return "il libro si legge..."

class Fantasy(Libreria):
    def __init__(self, editore, autore, titolo):
        super() .__init__(editore, autore)
        self.__titolo = titolo

    def Avvia (self):
        return f"Il libro {self.Info()} si legge..."

class Comics(Libreria):
    def Avvia(self):
        return f"I Comics{self.Info()} si vivono..."

fantasy = Fantasy("Mondadori", "Tolkien", "il signore degli anelli")
comics = Comics("Star Comics", "Naoko Takeuchi")

print(fantasy.Info())
print(fantasy.Avvia())

print(comics.Info())
print(comics.Avvia())
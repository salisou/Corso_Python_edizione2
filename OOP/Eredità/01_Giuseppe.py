class Player:
    def __init__(self, giocatore, squadra):
        self.giocatore = giocatore
        self.squadra = squadra

    def team(self):
        return f"Il giocatore {self.giocatore} della squadra {self.squadra}"

    def annuncio(self):
        return "Il giocatore gioca"


class Atleta(Player):
    def __init__(self, giocatore, squadra, ruolo):
        super().__init__(giocatore, squadra)
        self.ruolo = ruolo

    def annuncio(self):
        return f"{self.team()} gioca come {self.ruolo}"


player = Atleta("Mbappè", "Real Madrid", "Attaccante")

print(player.giocatore)
print(player.annuncio())

class ContoBancario:
    def __init__(self, saldo):
        self._saldo = saldo
    
    
    def deposita(self, importo):
        if importo > 0:
            self._saldo += importo
            print(f"Hai depositato questo importo {importo}")
        else:
            print(f"Importo non valido")
            
        
    def preleva(self, importo):
        if importo < 0:
            print(f"Importo non valido")
        elif importo > self._saldo:
            print(f"Saldo insufficente")
        else:
            self._saldo -= importo
            print(f"Saldo rimanente {self._saldo} €")
            
    
    def mostra_saldo(self):
        print(f"Saldo attuale: {self._saldo} €")



# --- programma principale---
print("\n=== CREA TUO CONTO BANCARIO ===")
saldo_iniziale = float(input("\nInserisci il saldo iniziale: "))

conto = ContoBancario(saldo_iniziale)

while True: 
    print("\n\n-------- MENU -\n\n")
    print("1. Deposita")
    print("2. Preleva")
    print("3. Mostra Saldo")
    print("0. Esci\n")
    
    scelta = input("Scegli un'opzione: ")
    
    if scelta == "1":
        importo = float(input("Quanto vuoi deposirare? "))
        conto.deposita(importo)
    
    elif scelta == "2":
        importo = float(input("Quanto vuoi prelevare? "))
        conto.preleva(importo)

    elif scelta == "3":
        conto.mostra_saldo()
    
    elif scelta == "0":
        print("Uscita del programma...")
        break
    
    else:
        print("Scelta non valida")
    
    
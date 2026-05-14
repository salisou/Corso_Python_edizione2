class Computer: # definisco la classe Computer
    def __init__(self, cpu, ram, hdd): # definisco il costruttore della classe Computer
        self._cpu = cpu # definisco la variabile cpu
        self._ram = ram # definisco la variabile ram
        self._hdd = hdd # definisco la variabile hdd
        
    def info(self): # definisco la funzione info()
        return f"Il computer ha: CPU {self._cpu}, {self._ram} di RAM e {self._hdd} di HDD" # definisco la funzione info()
    
computer = Computer(cpu="Intel", ram="16 GB", hdd="1 TB") # creazione della classe Computer
print(computer.info()) # stampa la stringa di informazioni della classe Computer

class Laptop(Computer):
    def __init__(self, cpu, ram, hdd, schermo): # definisco il costruttore della classe Laptop
        super().__init__(cpu, ram, hdd) # chiama la funzione di eredità di super()
        self._screen = schermo # definisco la variabile screen
        
    def info(self): # definisco la funzione info()
        return f"Il mio portatile ha una CPU {self._cpu}, {self._ram} di RAM, Harddisk da {self._hdd} e uno schermo da {self._screen} pollici" # definisco la funzione info()

class Steamdeck(Computer):
    def __init__(self, cpu, ram, hdd, schermo): # definisco il costruttore della classe Laptop
     super().__init__(cpu, ram, hdd) # chiama la funzione di eredità di super()
     self._screen = schermo # definisco la variabile screen
    
    def info(self): # definisco la funzione info()
        return f"Lo Steamdeck ha una CPU {self._cpu}, {self._ram} di RAM, un Harddisk da {self._hdd} e uno schermo da {self._screen} pollici" # definisco la funzione info()
    
class MiniComputer(Computer):
    def __init__(self, cpu, ram, hdd, gpu, schermo): # definisco il costruttore della classe Laptop
     super().__init__(cpu, ram, hdd) # chiama la funzione di eredità di super()
     self._screen = schermo # definisco la variabile screen
     self._gpu = gpu # definisco la variabile gpu
    
    def info(self): # definisco la funzione info()
        return f"Il minicomputer ha una CPU {self._cpu}, {self._ram} di RAM, una SSD da {self._hdd}, una GPU {self._gpu} e un monitor da {self._screen} pollici" # definisco la funzione info()

steam = Steamdeck(cpu="Zen 2 4c/8t", ram="16 GB", hdd="500 GB", schermo="7") 
laptop = Laptop(cpu="Intel", ram="16GB", hdd="500GB", schermo="15.6") 
mini=MiniComputer(cpu="AMD", ram="32 GB", hdd="1 TB", gpu="NVIDIA", schermo="27") 
print(steam.info()) 
print(laptop.info()) 
print(mini.info()) 
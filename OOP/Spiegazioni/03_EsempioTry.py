"""
    Excetion: con try / except
    try:
        # codice che potrebbe dare errore
    except:
        # cosa fare se c'è un errore
        
        ------------------------------------
    
     Excetion: con try / except ValueError / except / else
    try:
        # codice che potrebbe dare errore
    except ValueError:
        # cosa fare se c'è un errore
    except:
        # cosa fare se c'è un errore
    else:
        # cosa fare se non c'è un errore
        
        ------------------------------------
    
    Excetion: con try / except FileNotFoundError / finally
    try:
        # codice che potrebbe dare errore
    except FileNotFoundError:
        # cosa fare se c'è un errore
    finally:
        # cosa fare in ogni caso
"""

# Esempio1:
try:
    num1 = int(input("Inserisci il primo numero: "))
    print("Hai inserito -> ", num1)
except:
    print("Errore! devi inserire un numero intero.")
    
print("==================Fine programma 1! 🙂==================\n")

# Esempio2:
try:
    num1 = int(input("Inserisci un numero: "))
except ValueError:
    print("Errore! devi inserire un numero intero.")
except:
    print("Errore! devi inserire un numero intero.")
else:
    print("Hai inserito -> ", num1)

print("==================Fine programma 2! 🙂==================\n")


try:
    file = open("rubrica_contatti.txt", "r")
except FileNotFoundError:
    print("Il file non esiste!")
finally:
    print("Operazione treminata! 🙂")


print("==================Fine programma 3! 🙂==================\n")



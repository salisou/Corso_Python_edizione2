# Ecco il link del repository https://github.com/salisou/Corso_Python_edizione2.git

nome = "Luca"
print("Ciao " + nome) # concatenazione di stringhe

#================================================================================================

# tipi di dato in python
"""
    <class 'str'> = stringa
    <class 'int'> = intero
    <class 'float'> o decimale
    <class 'bool'> = booleano = condizione che restituisce (vero/falso)
"""
print('tipo del nome =>', type(nome))


#================================================================================================

# Gli operatori in python ( +, -, *, /, % )
num1 = 10
num2 = 3

print("Somma => ", num1 + num2)
print ("Sottrazione => ", num1 - num2)
print("Moltiplicazione => ", num1 * num2)
print("Divisione => ", num1 / num2) 
print("Resto => ", num1 % num2) 

#================================================================================================


# Input dell'utente
nome_uente = input("Inserisci il tuo nome: ")
eta = int(input("Quanti anni hai? "))
print("Ciao " + nome_uente + ", hai " + str(eta) + " anni")

#================================================================================================

# gli operatori di confronto (==, !=, >, <, >=, <=)
print(8 > 5) 
print(8 < 5)
print(8 >= 5)
print(8 <= 5)   
print(8 == 5)
print(8 != 5)

num_1 = int(input("Inserisci un numero: "))
num_2 = int(input("Inserisci un altro numero: "))

print("Il primo numero è uguale al secondo? ", num_1 == num_2)
print("Il primo numero è diverso dal secondo? ", num_1 != num_2)

#================================================================================================

# Operatori Logici (and, or, not)
print(True and False)
print(True or False)
print(not False)

#================================================================================================

# Condizioni (if, elif, else)
a = 10
b = 20

# Esempio 1: if semplice con else
if a > b:
    print("a è maggiore di b")
else:
    print("a non è maggiore di b")


# Esempio 2: if con elif e else
if a > b:
    print("a è maggiore di b")
elif a == b:
    print("a è uguale a b")
else:
    print("a è minore di b")

#================================================================================================
    
# il ciclo for in python
print("Ciao")
print("Ciao")
print("Ciao")
print("Ciao")
print("Ciao")

for i in range(5): # range(5) -> genera unmeri: 0,1,2,3,4
    print(f"Riga {i}") # parte da 0 => arriva a 4 (NON include 5)
    

variabile = "....." # o ''  
print()
lista = []
dictionary = {}
tupla = ()


path = "C:\\Users\\salis\\OneDrive\\Bureau\\Corso_Python_edizione2\\Base\\prova.py"
path2 = r"C:\Users\salis\OneDrive\Bureau\Corso_Python_edizione2\Base\prova.py" # r => raw string (stringa grezza)
print("\n\n============================================\n\n")



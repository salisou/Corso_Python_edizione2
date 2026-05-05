# Far inserire dati all'utente
# input() restituisce SEMPRE testo

nome = input('Come ti chiami? ') # chiediamo all'utente di inserire suo nome
print('Ciao piacere ', nome) # stampiamo facendo la concattenazione del testo

eta = int(input("Quanti anni hai? ")) # l'utente scrive 
print(f"Ho {eta} anni. L\'anno prossimo avrò {eta + 1} anni") # qui stampiamo i dati dell'utente 

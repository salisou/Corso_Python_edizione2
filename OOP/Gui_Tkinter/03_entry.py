import tkinter as tk
from openpyxl import Workbook, load_workbook
import os


root = tk.Tk()

# Titolo della finestra
root.title("Entry Form con Tkinter")

# Dimenzione della finestra
root.geometry("350x250")

# Colore sfondo della finestra
root.configure(background="#0A9142")

# creazione dell'entry
entry = tk.Entry(
    root,
    width=30,
    font=('Roboto', 16)
)

# entry.insert(0, "Inserisci il tuo nome")
entry.pack(pady=20)

# Metodo che legge i valori inseriti dall'utente
def legge_testo():
    nome = entry.get()
    print(f"Ti chiami {nome}")
    
# crea il bottone Salva
button = tk.Button(
    root,
    text='Salva',
    command=legge_testo
)
button.pack(pady=10)

# avvio app
root.mainloop()
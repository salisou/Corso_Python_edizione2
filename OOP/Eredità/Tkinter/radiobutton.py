import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

# Titolo della finestra
root.title("Imparo a usare Tkinter")

# la dimenzione della form
root.geometry("800x750")

# il colore dello sfondo
root.configure(bg="#072E2D")

root.geometry("800x750+200+200")

root.resizable(False, False)

root.minsize(350, 500)



# Checkbutton — variabile collegata BooleanVar
var_check = tk.BooleanVar()
check = tk.Checkbutton(root, 
                       fg="white",
                       text="Accetta termini",
                       variable=var_check, 
                       background="#072E2D",
                       selectcolor="#072E2D"
                       )
check.pack(pady=10)




# per domani crea una lista dei linguaggi 
linguaggi = [
    ("Python","python"),
    ("Java","java"),
    ("Html","html"),
    ("CSS","css"),
    ("PHP","php"),
    ("C#","sharp"),
    ("C++","cpp"),
    ("JavaScript","js"),
    ("Delphy","pascal"),
    ("MongoDb","NoSql"),
    ("SQL Server","t-sql")
]

var_radio = tk.StringVar(value="python")

# ciclo for per recuperare la testo e valore
# Radiobutton — variabile collegata StringVar
for testo , valore in linguaggi:
    tk.Radiobutton(root, 
                fg="white",
                text=testo,
                value=valore, 
                variable=var_radio, 
                bg="#072E2D", 
                selectcolor="#072E2D"
                ).pack(padx=20, anchor="w")

def mostra():
    messagebox.showinfo("Selezione", 
                        f"Accetta termini: {var_check.get()}\n"
                        f"Linguaggio scelto: {var_radio.get()}")

tk.Button(root, text="Mostra selezione", command=mostra).pack(pady=20)
root.mainloop()
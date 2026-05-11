import tkinter as tk

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

root.mainloop()
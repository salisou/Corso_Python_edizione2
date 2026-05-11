import tkinter as tk

root = tk.Tk() 

# Titolo della finestra
root.title("Imparo a usare Tkinter")

root.geometry("800x750")

root.configure(bg="#0DA3A1")

root.geometry("800x750+200+200")

root.resizable(False, True)

root.minsize(350, 500)

root.mainloop()
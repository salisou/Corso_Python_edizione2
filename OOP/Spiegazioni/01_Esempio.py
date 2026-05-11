import tkinter as tk


class App:
    def __init__(self):

        root = tk.Tk() 

        # Titolo della finestra
        root.title("Imparo a usare Tkinter")

        # Crea una Label
        tk.Label(
            root,                          # contenitore padre
            text="Ciao, Tkinter! 👋",
            font=("Arial", 20, "bold"),  # (font, dimensione, stile)
            fg="#fff",                  # colore testo (foreground)
            bg="#072E2D"                   # colore sfondo
        ).pack(padx=20, pady=20)

        # la dimenzione della form
        root.geometry("800x750")

        # il colore dello sfondo
        root.configure(bg="#072E2D")

        root.geometry("800x750+200+200")

        root.resizable(False, False)

        root.minsize(350, 500)

        root.mainloop()

App()
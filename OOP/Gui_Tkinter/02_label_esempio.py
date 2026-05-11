import tkinter as tk

root = tk.Tk() 

# Titolo della finestra
root.title("Label form")

root.geometry("800x750")

root.configure(bg="#0DA3A1")

tk.Label(
        root,
        text="Ecco come sto imparando Tkinter😅",
        font=("Roboto", 30, "italic"),
        bg="#0DA3A1",
        fg="#fff",
        cursor="hand2"
    ).pack(pady=20)


root.geometry("800x750+200+200")

root.resizable(False, True)

root.minsize(350, 500)

root.mainloop()
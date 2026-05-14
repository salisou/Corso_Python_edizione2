# Importazione dei packetti
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class App:
    def __init__(self):
        # Finestra principale
        self.root = tk.Tk()
        self.root.title("Grafico con Tkinter + Matplotlib + OOP")
        self.root.geometry("800x600")
        
        # Frame superiore (bottoni)
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=20)
        
        # Bottone per generare il grafico
        btn = tk.Button(top_frame, text="Genera grafico", command=self.genera_grafico)
        btn.pack()
        
        # Frame per il grafico
        self.graph_frame = tk.Frame(self.root)
        self.graph_frame.pack(fill="both", expand=True)

    def genera_grafico(self):
        # cancella il grafico precedente
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
            
        # Dati di esempio fack o db / json, Excel, CSV, PDF, DOC....
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        y = [10, 20, 30, 40, 25, 35, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110]
        
        # Creazione figura MatplotLib
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x, y, marker='o', color='blue')
        ax.set_title("Andamento Valori")
        ax.set_xlabel("Etichette X")
        ax.set_ylabel("Etichette Y")
        
        # Inserimento grafico in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
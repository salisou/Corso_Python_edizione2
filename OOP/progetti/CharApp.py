import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class CharApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Application Grafic Excel")
        self.geometry("1000x650")
        
        self.df = None # DataFrame vuoto
        
        self.create_widgets()
    
    def create_widgets(self):
        # pulsante per caricare il file Excel
        ttk.Button(self, text="📂 Carica File Excel", command=self.load_excel).pack(pady=10)
        
        
        # Dropdown tipo grafico
        self.chart_type = tk.StringVar(value="Bar Chart")
        
        ttk.Label(self, text="Tipo Grafico: ", font=("Helvetica", 12)).pack()
    
        lista = ["Bar Chart", "Line Chart", "Pie Chart"]
        ttk.Combobox(self,
                     textvariable=self.chart_type,
                     values= lista,
                     state="readonly",
                     width=20
                     ).pack(pady=10)

        # Pulsante genera grafico
        ttk.Button(self,
                   text="📊 Genera Grafico",
                   command=self.generate_chart).pack(pady=5)
        
        
        # Aria Grafico
        self.chart_area = tk.Frame(self)
        self.chart_area.pack(fill="both", expand=True)
   
    def load_excel(self):
        """Carica il file Excel e la salva ne DataFrame"""
        file_Path = filedialog.askopenfilename(
            title="Seleziona file Excel",
            filetypes=[("Excel files", "*.xlsx", "*.xls")]
        )
        
        if not file_Path:
            return

        try:
            self.df = pd.read_excel(file_Path)
            messagebox.showinfo("Successo", "File Excel caricato con successo!")
            print(self.df.head())
        except Exception as e:
            messagebox.showerror("Errero", f"Inpossibile caricare il file \n{e}")

    def generate_chart(self):
            """Genera il grafico in base al tipo selezionato"""
            if self.df is None:
                messagebox.showwarning("⚠️ Attenzione", "Prima caricare il file Excel!")
                return
            
            # Pulizia aria grafico
            for widget in self.chart_area.winfo_children():
                widget.destroy()
            
            # ============ Da continuare
            
            #Usa le prime due colonne del DataFrame
            col1 = self.df.columns[0]
            col2 = self.df.columns[1]
            

        
        
# avvio lapplicazione
if __name__ == "__main__":
    app = CharApp()
    app.mainloop()
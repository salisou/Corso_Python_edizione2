import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Todo-List")
root.geometry("600x500")
root.configure(bg="#0A2F3C")

# Entry
entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=25)

entry.pack(pady=10)


# funzioni operazione CRUD (Create, Read, Update, Delete)
def aggiungi():
    testo = entry.get().strip()
    if testo:
        lb.insert(tk.END, testo)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Attenzione", "Inserisci un attività")

def mostra():
    idx = lb.curselection()
    if idx:
        messagebox.showwarning("Attenzione", "Seleziona un attività", lb.get(idx[0]))
    else:
        messagebox.showinfo("Info", "Nessuna attività selezionata")
        
def rimuovi():
    idx = lb.curselection()
    if idx:
        lb.delete(idx[0])
    else:
        messagebox.showwarning("Attenzione", "nessuna attività selezionata")

def modifica():
    idx = lb.curselection()
    nuovo_testo = entry.get().strip()
    
    if not idx:
        messagebox.showwarning("Errore", "Nessuna attività selezionata")
        return
    
    if not nuovo_testo:
        messagebox.showwarning("Errore", "Inserisci un nuovo testo")
        return
    
    lb.delete(idx[0])
    lb.insert(idx[0], nuovo_testo)
    entry.delete(0, tk.END)
 
def carca_in_entry(event):
    idx = lb.curselection()
    if idx:
        entry.delete(0, tk.END)
        entry.insert(idx[0], lb.get(idx[0]))
        
# Frame con listbox + scrollbar
frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

#Bottoni
tk.Button(frame_btn, 
          text="Aggiungi",
           width=12,
           font=("Arial", 12),
          command=aggiungi).grid(row=0, column=0, padx=5, pady=5)

tk.Button(frame_btn, 
          text="Modifica",
           width=12,
           font=("Arial", 12),
          command=modifica).grid(row=0, column=1, padx=5, pady=5)

tk.Button(frame_btn, 
          text="Elimina",
          width=12,
          font=("Arial", 12),
          command=rimuovi).grid(row=0, column=2, padx=5, pady=5)

tk.Button(frame_btn, 
          text="Mostra selezione",
          width=12,
          font=("Arial", 12),
          command=mostra).grid(row=0, column=3, padx=5, pady=5)

frame_lit = tk.Frame(root)
frame_lit.pack(pady=10)

# Scrollbar
scrollbar = tk.Scrollbar(frame_lit, orient="vertical")


lb = tk.Listbox(frame_lit,
                height=10, 
                width=30,
                font=("Arial", 14),
                yscrollcommand=scrollbar.set)

scrollbar.config(command=lb.yview)

lb.pack(side="left")
scrollbar.pack(side="right", fill="y")

lb.bind("<<ListboxSelect>>", carca_in_entry)

root.mainloop()
"""
    Recuperare automaticamente tutte le tabelle da SQL Server con Python
"""

import pyodbc as odbc
import pandas as pd

# StrConn => per la connessione al database 
strCon = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=Moussa\\SQLEXPRESS;"
    "DATABASE=AziendaDb;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

try:
    print("⏳ Connessione al server...")
    
    conn = odbc.connect(strCon)
    cursor = conn.cursor()
    
    print(f"🗃️ Recupero automaticamente delle tabelle\n")
    
    # Esecuzione della store procedure
    cursor.execute("EXEC sp_ListaTabelle")
    tabelle = [row[0] for row in cursor.fetchall()]

    print("📌 Tabelle trovate:\n")
    for t in tabelle:
        print(f" → {t}")
        
    # File Excel finale
    writer = pd.ExcelWriter("RaportoAziendaDb.xlsx", engine="xlsxwriter")
    
    # ciclo per ogni tabella
    for tabella in tabelle:
        print(f"Elaboro tabella: {tabella}")
        
        try:
            query = f"SELECT * FROM [{tabella}]"
            df = pd.read_sql(query, conn)   
            
            # Conversione colonne binarie
            for col in df.columns:
                if df[col].dtype == object:
                    df[col] = df[col].apply(
                        lambda x: "<BINARY DATA>" 
                            if isinstance(x, bytes) else x
                    )

            # Scrittura nel file Excel
            df.to_excel(writer, sheet_name=tabella[:31], index=False)
            print(f"   ✔ Salvata nel foglio: {tabella[:31]}")
        
        except Exception as e:
            print(f"❌ Errore nella tabella {tabella}: {e}")
            
    writer.close()
    print("\n📁 File Excel generato: RaportoDatabase.xlsx")

except Exception as ex:
    print(f"Errore di connessione: {ex}")

finally:
    try:
        conn.close()
        print("Connessione chiusa.")
    except:
        print("⚠️ Impossibile chiudere la connessione.")

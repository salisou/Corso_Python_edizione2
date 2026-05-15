"""
    select @@SERVERNAME as NomeServer
    select @@VERSION as Vezione 

    Recuperare automaticamente tutte le tabelle da SQL Server con Python
    
    Obiettivo del corso:
        collegarsi a un database SQL Server
        eseguire query di sistema
        recuperare automaticamente tutte le tabelle
        gestire errori e connessioni in modo professionale
        capire come un Data Analyst esplora un database sconosciuto
"""
 
# istallazione del pyodbc e pandas (install pyodbc pandas)
import pyodbc as odbc
import pandas as pd


conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=Moussa\\SQLEXPRESS01;"
    "DATABASE=ScuolaDb;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

try:
    print("⏳ Connessione al server...")
    
    conn = odbc.connect(conn_str)
    cursor = conn.cursor()
    
    values = cursor.execute('SELECT @@SERVERNAME').fetchone()[0]
    print(f"✅ Connesso al server {values}\n")
    
    print("\n Recupera automaticamente tutte le tabelle ")
    
    # VERSIONE 1
    # cursor.execute("""
    #     SELECT TABLE_NAME 
    #     FROM INFORMATION_SCHEMA.TABLES
    #     WHERE TABLE_TYPE='BASE TABLE'
    #     ORDER BY TABLE_NAME ASC
    #     """
    # )
    
    # VERSIONE 2
    cursor.execute("EXEC sp_ListaTabelle")
    
    # VERSIONE 3 CON PANDAS
    # df = pd.read_sql("EXEC sp_ListaTabelle", conn)
    # print(df)
    
    tabelle = [row[0] for row in cursor.fetchall()]
    print("📌 Tabella Trovate\n")
    
    for row in cursor.fetchall():
         print(f" -> {row[0]}")
    
    print("📊 LETTURA TABELLE")
    
    for tabella in tabelle:
        print("=========================================")
        print(f"📌 Tabelle {tabella}")
        print("=========================================")
        
        try:
            query = f"SELECT * FROM {tabella}"
            cursor.execute(query)

            colonne = [desc[0] for desc in cursor.description]
            print(f"Colonne trovate: {colonne}")
            # =========================
            rows = cursor.fetchall()
            
            
            for row in rows:
                print(row)
          # ====================
        except Exception:
            print("Attenzione Moussa")
        
except Exception as e:
    print("❌ Errore di connessione:")
    print(e)

finally:
    try:
        print("Chiusura connessione...\n")
        conn.close()
        print("🔐 Connessione chiusa.")
    except:
        print("Riprova!")
        pass
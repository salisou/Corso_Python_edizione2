import pyodbc as odbc
import pandas as pd

strCon = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=Moussa\\SQLEXPRESS;"
    "DATABASE=ScuolaDb;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

try:
    print("⏳ Connessione al server...")

    conn = odbc.connect(strCon)
    cursor = conn.cursor()

    print("📚 Recupero delle tabelle dal database...\n")

    cursor.execute("EXEC sp_ListaTabelle")

    tabelle = [row[0] for row in cursor.fetchall()]

    print("📌 Tabelle trovate:")
    for t in tabelle:
        print(" →", t)

    print("\n📁 Esportazione delle tabelle in file Excel...\n")

    for tabella in tabelle:
        print(f"📌 Esporto tabella: {tabella}")

        try:
            query = f"SELECT * FROM [{tabella}]"
            df = pd.read_sql(query, conn)

            # Conversione colonne binarie
            for col in df.columns:
                if df[col].dtype == object:
                    df[col] = df[col].apply(
                        lambda x: "<BINARY DATA>" if isinstance(x, bytes) else x
                    )

            file_name = f"{tabella}.xlsx"

            # Usa xlsxwriter per evitare openpyxl
            df.to_excel(file_name, index=False, engine="xlsxwriter")

            print(f"   ✔ Salvata in: {file_name}")

        except Exception as e:
            print(f"   ❌ Errore nella tabella {tabella}: {e}")

    print("\n🎉 Esportazione completata!")

except Exception as e:
    print("❌ Errore di connessione:")
    print(e)

finally:
    try:
        conn.close()
        print("\n🔐 Connessione chiusa.")
    except:
        print("⚠️ Impossibile chiudere la connessione.")

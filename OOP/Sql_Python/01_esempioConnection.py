import pyodbc as odbc


# ── Autenticazione Windows (Trusted Connection) ──
conn_str_windows = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=Moussa\SQLEXPRESS01;"          
    "DATABASE=ScuolaDb;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)


conn = odbc.connect(conn_str_windows)
print("✅ Connesso a SQL Server!")
#### Active containers:
<P>
mssql_fixed: SQL Server 2025 on 1433 ✓ (ready)
sql_server_container: SQL Server 2025 on 1434 ✓ (ready)
welcome-to-docker: Demo app on 8088 ✓ (ready)
To connect remotely (from your app), use: Server=localhost;User Id=sa;Password=MyP@ssw0rd123;Encrypt=true;TrustServerCertificate=true;Connection Timeout=30;
</P>

Next, you can create databases or test with a client tool.

Your SA password is 'MyP@ssw0rd123' — it's stored in the container's environment variables.

If you've forgotten a different SQL user's password, you can reset it via the SA account:
        docker exec mssql_fixed bash -c '/opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P "MyP@ssw0rd123" -C -Q "ALTER LOGIN [username] WITH PASSWORD = '\''NewPassword123!'\'';"'
Replace username and NewPassword123! with your target user and new password (must be 8+ chars with uppercase, lowercase, digit, symbol).

If you lost the SA password itself, you must:

Stop the container: 
        docker stop mssql_fixed
--
Remove it: docker rm mssql_fixed
Run a new one with a password you remember: 
        docker run -d -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=YourNewPassword123!" -p 1433:1433 --name mssql_fixed mcr.microsoft.com/mssql/server:2025-latest

Replace username with the actual user you want to reset.

If you forgot the SA password, you cannot recover it. You must reset the container.

Run these commands:
        docker stop mssql_fixed
        docker rm mssql_fixed
--
Then create a new container with a password you'll remember:
        docker run -d -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=MyNewPassword123!" -p 1433:1433 --name mssql_fixed mcr.microsoft.com/mssql/server:2025-latest

Replace MyNewPassword123! with your own password (must be 8+ characters with uppercase, lowercase, digits, and symbols).

Note: This will delete all databases in the old container. If you have data you need, back it up first.

use a password without the ! symbol:

Your new container XXXXXXXXXXX is running. Verify it:
        docker ps
Then test the connection with your new password MyNewPassword@123:
        docker exec mssql_fixed /opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P MyNewPassword@123 -C -Q "SELECT @@VERSION"

--

        import pyodbc as odbc
        import pandas as pd

        conn_str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost,1433;"
            "DATABASE=master;"
            "UID=sa;"
            "PWD=MyNewPassword@123;"
            "TrustServerCertificate=yes"
        )

        try:
            conn = odbc.connect(conn_str)
            print(f"✅ Connesso al server")
            conn.close()
        except Exception as e:
            print("❌ Errore di connessione:")
            print(e)
    
    
Key changes:
        SERVER=localhost,1433 (not container ID)
        PWD=MyNewPassword@123 (your actual password)
        No spaces around =
        Removed duplicate TrustServerCertificate
Try this and let me know if it works!

        ❌ Errore di connessione: ('01000', "[01000] [unixODBC][Driver Manager]Can't open lib 'ODBC Driver 17 for SQL Server' : file not found (0) (SQLDriverConnect)")

The ODBC driver for SQL Server is not installed on your system. Install it:

macOS:
        brew install unixodbc msodbcsql17

Linux (Ubuntu/Debian):
        sudo apt-get update
        sudo apt-get install unixodbc unixodbc-dev
        curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
        sudo apt-get install msodbcsql17

Linux (Red Hat/CentOS):
        sudo yum install unixODBC unixODBC-devel
        sudo yum install msodbcsql17

Windows: 
- Download and install from: https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server

odbcinst -j
Then try your Python connection again.

Alternatively, use pyodbc with pymssql (simpler for Docker):

        import pymssql

        try:
            conn = pymssql.connect(
                server='localhost',
                user='sa',
                password='MyNewPassword@123',
                database='master'
            )
            print("✅ Connesso al server")
            conn.close()
        except Exception as e:
            print("❌ Errore di connessione:")
            print(e)


Install pymssql: 
        pip install pymssql

After installation, verify:
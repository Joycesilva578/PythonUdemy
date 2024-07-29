import pyodbc

def get_connection_string():
    server = 'DESKTOP-1UIC940'
    database = 'crud'
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'
    return connection_string

def connect_db():
    try:
        connection_string = get_connection_string()
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        return conn, cursor
    except pyodbc.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None, None

#testando
conn, cursor = connect_db()
if conn and cursor:
    print('Conexão estabelecida com sucesso')
else:
    print('Conexão não encontrada')

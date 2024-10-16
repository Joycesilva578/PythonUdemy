import pandas as pd
import requests
from conexaoMysql import conexao_mysql


login = 'joyce.hora@grupovamos.com.br'
token = 'seu_token_aqui.'

def createtable(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS GestaoPagamentoCheckPoint (
        Id INTEGER PRIMARY KEY AUTO_INCREMENT,
        NomeColaborador varchar(50) null,
        Estimativa VARCHAR(50) NULL,
        Valor_Esperado decimal(10,2) null,
        Empresa varchar(50) null,
        Card varchar(50) null,
        Status varchar(30) null,
        Data_Criacao datetime null,
        Consultoria varchar(50) null,
        Atividade varchar(100) null,
        Mes varchar(50) null
        )""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS GestaoPagamento (
            Id INTEGER not null ,
            NomeColaborador varchar(50) null,
            Estimativa VARCHAR(50) NULL,
            Valor_Esperado decimal (13,4) null,
            Faturado VARCHAR(50) NULL,
            Empresa varchar(50) null,
            Card varchar(50) null,
            Status varchar(30) null,
            Data_Criacao datetime null,
            Consultoria varchar(50) null,
            Atividade varchar(50) null,
            Mes varchar(50) null
            )""")

def readexcel(cursor,excel):
    df = pd.read_excel(excel,sheet_name="teste")
    for index, row in df.fillna(0).iterrows():
        cursor.execute("""
           INSERT INTO GestaoPagamentoCheckPoint (NomeColaborador, Estimativa,Valor_Esperado, Empresa, Card, Status,Data_Criacao,Consultoria,Atividade,Mes)
            VALUES (%s,%s, %s, %s, %s, %s, %s, %s,%s,%s)
           """, (
            row['Responsavel'],
            row['Estimativa'],
            row['Valor Esperado'],
            row['Empresa'],
            row['Chave'],
            row['Status'],
            row['Criado'],
            row['Consultoria'],
            row['Resumo'],
            row['Mes']
        ))

def processacampo(dataframe, cursor):
    for index, row in dataframe.fillna('0').iterrows():
        print(index)
        timeoriginalestimate = row.get('fields.timeoriginalestimate')
        Faturado = row.get('fields.customfield_11382.value')
        try:
            timeoriginalestimate = int(timeoriginalestimate)
            Faturado = int(Faturado)

        except (TypeError, ValueError):
            timeoriginalestimate = 0

        timee = timeoriginalestimate // 3600
        timee = 'Esforco Nao Informado' if timee == 0 else timee

        Faturado = 'Faturado Nao Informado' if Faturado == 0 else Faturado
        ValorTotal = timee * 115

        cursor.execute("""
            INSERT IGNORE INTO GestaoPagamento (Id,Estimativa,ValorTotal,Faturado, Empresa, Card, STATUS, Data_Criacao, Consultoria, Atividade)
            VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s)""", (
                row.get('id'),  # id
                timee,  # ESFORCO
                ValorTotal,
                Faturado,  # Faturado
                row.get('fields.customfield_10607'),  # empresa
                row.get('key'),  # TIPO_PROJETO
                row.get('fields.status.name'),  # Status
                row.get('fields.created'),  # DATA_CRIACAO
                row.get('fields.project.name'),  # PROJETO
                row.get('fields.summary')  # atividade

                ))

def projetojson(projeto):
    url = f'https://grupovamos.atlassian.net/rest/api/2/search?jql=project={projeto}'
    response = requests.get(url, auth=(login, token))

    if response.status_code == 200:
        return pd.json_normalize(response.json()['issues'])

def exportexcel(cursor):
    cursor.execute("""SELECT * FROM GestaoPagamento """)
    rown = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    df_sql = pd.DataFrame(rown, columns=columns)
    df_sql.to_excel('C:/Users/joyce.hora/Documents/gestaopagamento/GestaoPagamento.xlsx',
                    index=False, sheet_name='PROJETOS')
def processaprojeto(projeto):
    conn = conexao_mysql()
    cursor = conn.cursor()

    createtable(cursor)
    readexcel(cursor,r'C:\Users\joyce.hora\Documents\gestaopagamento\Bamse_competencia_Julho_2024.xlsx')

    dataframe = projetojson(projeto)
    processacampo(dataframe,cursor)
    exportexcel(cursor)

    conn.commit()
    cursor.close()
    conn.close()




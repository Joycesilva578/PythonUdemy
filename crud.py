def create(cursor,name,cpf):
    insert_sql = "Insert Into PessoasFisicas (Name, CPF) Values(?,?)"
    cursor.execute(insert_sql,(name,cpf))
    cursor.connection.commit()
    print('Registro Criado')

def read(cursor):
    read_sql = "Select * From PessoasFisicas"
    cursor.execute(read_sql)
    rows = cursor.fetchall()
    print(rows)
def update(cursor, name,cpf,id):
    update_sql = "UPDATE PessoasFisicas SET Name = ?, CPF = ? WHERE Id = ?"
    cursor.execute(update_sql, (name,cpf,id))
    cursor.connection.commit()
    print('Registro atualizado')
def delete(cursor, id):
    delete_sql = "DELETE FROM PessoasFisicas WHERE Id = ?"
    cursor.execute(delete_sql, (id,))
    cursor.connection.commit()
    print('Registro excluído')

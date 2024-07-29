from conexao import connect_db
import crud

if __name__ == "__main__":
    conn, cursor = connect_db()

    # crud.create(cursor,'Joyce Silva da Hora', 48010978809),
    # crud.create(cursor,'Joelma da Silva Lima', 18697277892)
    # crud.create(cursor,'Roberio Ferreira da Hora', 17636985802)
    # crud.create(cursor,'Matheus Silva da Hora', 123456789)

    crud.read(cursor)

    # crud.update(cursor, 'Joyce Hora', 48010978809,1)
    # crud.update(cursor, 'Joelma Lima', 18697277892,2)
    # crud.update(cursor, 'Roberio Hora', 17636985802,3)
    # crud.update(cursor, 'Matheus Hora', 123456789,4)

    ##crud.delete(cursor, 1)

    cursor.close()
    conn.close()

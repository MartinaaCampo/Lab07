from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def read_biblioteca_db(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connessione stabilita")
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT * FROM biblioteca "
            cursor.execute(query)
            result = []
            for riga in cursor:
                result.append(Biblioteca(riga["id"],riga["nome"],riga["indirizzo"]))
            cursor.close()
            cnx.close()
            return result

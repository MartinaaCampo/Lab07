from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def read_libri_db(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is not None:
            print("Connessione stabilita")
            cursor = cnx.cursor(dictionary=True)
            query="SELECT DISTINCT genere FROM libro ORDER BY genere"
            cursor.execute(query)
            for riga in cursor:
                result.append(riga["genere"])
            cursor.close()
            cnx.close()
            return result

    def read_libri_filtrati_db(self, id_biblioteca,genere):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is not None:
            print("Connessione stabilita")
            query="SELECT * FROM libro WHERE id_biblioteca = COALESCE(%s, id_biblioteca) AND genere = COALESCE(%s, genere)"
            cursor=cnx.cursor()
            cursor.execute(query,(id_biblioteca, genere))
            for riga in cursor:
                result.append(Libro(riga[0],riga[1],riga[2],riga[3],riga[4], riga[5]))
            cursor.close()
            cnx.close()
            return result

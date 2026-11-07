from database.DB_connect import DBConnect as DB
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def get_libri_from_db(self):
         query = "SELECT * FROM libro"
         cnx = DB.get_connection()
         cursor = cnx.cursor()
         cursor.execute(query)

         lista_libri = []
         for libro in cursor:
             lista_libri.append(Libro(*libro))
         cursor.close()
         cnx.close()
         return lista_libri
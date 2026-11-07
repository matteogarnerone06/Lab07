from database.DB_connect import DBConnect as DB
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def get_biblioteca(self):
        query = "SELECT * FROM biblioteca"
        cnx = DB.get_connection()
        cursor = cnx.cursor()
        cursor.execute(query)
        tutto = cursor.fetchall()
        cursor.close()
        cnx.close()
        return tutto


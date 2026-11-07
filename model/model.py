from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO
from model.biblioteca_DTO import Biblioteca

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()
        self.lista_libri_filtrati = []
        self._lista_biblioteche = []
        self._lista_generi = []
        self.get_biblioteche()
        self.get_generi()


    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        # TODO
        self.lista_libri_filtrati = []
        for i in self._lista_biblioteche:

            if i.nome== biblioteca:

                for libri in self._libro_dao.get_libri_from_db():
                    if libri.genere == genere:

                        self.lista_libri_filtrati.append(libri)

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        # TODO
        if len(self._lista_generi) == 0:
            for libro in self._libro_dao.get_libri_from_db():
                if libro.genere not in self._lista_generi:
                    key = libro.genere
                    self._lista_generi.append(key)



    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # TODO
        if len(self._lista_biblioteche) == 0:
            for biblioteca in self._biblioteca_dao.get_biblioteca():
                self._lista_biblioteche.append(Biblioteca(*biblioteca))


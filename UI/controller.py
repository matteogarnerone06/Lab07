from sys import excepthook

import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dd_biblioteca(self,scelta_biblioteca):
        for i in self._model._lista_biblioteche:
            scelta_biblioteca.options.append(ft.DropdownOption(key = i.nome, text = i.nome))

        return scelta_biblioteca

    def popola_dd_genere(self,scelta_genere):

        for i in self._model._lista_generi:
            scelta_genere.options.append(
                ft.DropdownOption(key=i, text=i)
            )
        return scelta_genere

    # CALLBACKS DROPDOWN
    # TODO
    def scelta_biblioteca(self, scelta):
        if scelta.data != "Nessun opzione":
            self.biblioteca_selezionata = scelta
        else:
            self.biblioteca_selezionata = None
        self._view.listview.controls.clear()
        print("biblioteca_selezionata")

    def scelta_genere(self, scelta):
        if scelta.data != "Nessun opzione":
            self.genere_selezionato = scelta
        else:
            self.genere_selezionato = None
        self._view.listview.controls.clear()
        print("genere_selezionato")

    # AZIONE: MOSTRA LIBRI
    # TODO
    def mostra(self):
        print("cliccato mostra")
        try:
            if self.biblioteca_selezionata is not None and self.genere_selezionato is not None:
                self._model.get_libri_filtrati(self.biblioteca_selezionata.data, self.genere_selezionato.data)
            else:
                self._view.show_alert("Seleziona sia una biblioteca che un genere!")
                return

            self._view.listview.controls.clear()

            if len(self._model.lista_libri_filtrati) != 0:
                for libro in self._model.lista_libri_filtrati:
                    self._view.listview.controls.append(ft.Text(f"{libro}"))
            else:
                self._view.show_alert("Nessun libro trovato con questi filtri.")

            self._view.update()

        except Exception as ex:
            self._view.show_alert(f"Errore imprevisto: {ex}")



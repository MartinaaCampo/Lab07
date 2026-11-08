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
    def popola_dropdowns(self):
        biblioteche=self._model.get_biblioteche()
        self._view.dd_biblioteca.options.append(ft.dropdown.Option(key="None", text="Nessun filtro"))
        for b in biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(key=str(b.id), text=b.nome))

        generi=self._model.get_generi()
        self._view.dd_genere.options.append(ft.dropdown.Option(key="None", text="Nessun filtro"))
        for g in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(key=g, text=g))

        self._view.update()
    # CALLBACKS DROPDOWN
    def handle_dropdown_change(self, e):
        pass

    # AZIONE: MOSTRA LIBRI
    def handler_btn(self,e):
        id_biblio_selezionata=self._view.dd_biblioteca.value
        id_genere_selezionato= self._view.dd_genere.value

        if id_biblio_selezionata=="None" or id_biblio_selezionata is None:
            id_biblio_selezionata=None
        else:
            id_biblio_selezionata=int(id_biblio_selezionata)
        if id_genere_selezionato=="None" or id_genere_selezionato is None:
            id_genere_selezionato=None

        libri = self._model.get_libri_filtrati(id_biblio_selezionata, id_genere_selezionato)
        self._view.list_libri.controls.clear()
        for libro in libri:
            self._view.list_libri.controls.append(ft.Text(f"{libro.titolo} - {libro.autore} ({libro.anno_pubblicazione})"))
        self._view.update()























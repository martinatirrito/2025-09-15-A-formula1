import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handleCreaGrafo(self,e):
        self._model.buildGraph(self._view._ddAnno1.value, self._view._ddAnno2.value)
        Nnodes, Nedges = self._model.getGraphDetails()

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f'Grafo correttamente creato.'
                                                      f'Il grafo contiene {Nnodes} nodi e {Nedges} archi.'))
        self._view.update_page()

    def handleDettagli(self, e):
        top3 = self._model.getTop3Archi()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f'Archi di peso maggiore:', color = "red"))
        for a in top3:
            self._view.txt_result.controls.append(ft.Text(f'{a[0]} -> {a[1]}(peso: {a[2]["weight"]})'))

        numero, largest, details = self._model.getConnessaInfo()
        self._view.txt_result.controls.append(ft.Text(f'Il grafo contiene {numero} componenti connesse.', color = "red"))

        self._view.txt_result.controls.append(ft.Text(f'La componenete connessa maggiore ha dimensione pari a {len(largest)}:', color = "red"))
        for l in largest:
            self._view.txt_result.controls.append(ft.Text(f'{l}'))

        self._view.txt_result.controls.append(ft.Text(f'Componente connessa in ordine decrescente in grado dei nodi.', color = "red"))
        for d in details:
            self._view.txt_result.controls.append(
                ft.Text(f'{d[0]} - grado: {d[1]}'))

        self._view.update_page()

    def handleCerca(self, e):
        pass


    def fillDDYears(self): #PUNTO 1
        years = self._model.getAllYears()
        for y in years:
            self._view._ddAnno1.options.append(ft.dropdown.Option(y))
            self._view._ddAnno2.options.append(ft.dropdown.Option(y))
        self._view.update_page()




import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._idMapDrivers = {}
        self._drivers = []


    def buildGraph(self, year1, year2):
        self._graph.clear()
        self._drivers = DAO.getAllNodes(year1, year2)
        for d in self._drivers:
            self._idMapDrivers[d.driverId] = d
        self._graph.add_nodes_from(self._drivers)

        edges = DAO.getAllEdges(year1, year2, self._idMapDrivers)
        for e in edges:
            self._graph.add_edge(e.d1, e.d2, weight = e.peso)


    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getTop3Archi(self): #3 archi di peso maggiore
        return sorted(self._graph.edges(data = True), key = lambda x: x[2]["weight"], reverse = True)[:3]

    def getConnessaInfo(self):
        components = list(nx.connected_components(self._graph)) #len --> numero componenti connesse
        largest = max(components, key = len) #usa la dimensione della componente per decidere qual è la più grande. Mi da tutti i nodi

        #ordino in senso decrescente secondo il grado dei nodi
        #prendo sotto grafo che ha la componente connessa come grafo
        subgraph = self._graph.subgraph(largest).copy()

        orderedNodes = sorted(subgraph.nodes(), key = lambda n: self._graph.degree(n), reverse = True) #dato nodo n restituisco il grado
                                                                                                    #cosi ho i nodi da grado maggiore a minore

        details = [(n, self._graph.degree(n)) for n in orderedNodes]

        return len(components), largest, details


    def getAllYears(self):  #punto 1
        return DAO.getAllYears()

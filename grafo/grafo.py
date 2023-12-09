import networkx as nx
import matplotlib.pyplot as plt


class Grafo:

    def __init__(self):
        self.grafo = nx.Graph()


    def addNodo(self,nodo):
        self.grafo.add_node(nodo)


    def addAresta(self,origem,destino,peso):
        self.grafo.add_edge(origem,destino,distancia = peso)

    
    def plot(self):

        layout = nx.spring_layout(self.grafo)
        etiquetas = {(i, j): self.grafo[i][j]['distancia'] for i, j in self.grafo.edges()}

        nx.draw(
            self.grafo,
            layout,
            with_labels = True,
            node_size = 700,
            node_color = "skyblue",
            font_size = 10,
            font_color = "black",
            font_weight = "bold",
            edge_color = "gray",
            linewidths = 1)

        nx.draw_networkx_edge_labels(
            self.grafo,
            layout,
            edge_labels = etiquetas,
            font_size = 10,
            font_color = "black")
        
        plt.show()

    
    def get(self):

        aa, bb = self.grafo["Faria"]

        print(self.grafo["Faria"])
        print(aa)
        print(bb)

        print(self.grafo["Faria"][aa]["distancia"])
        print(bb)


    
    def dijkstraAll(self,origem):

        distanciasLista = {nodo: float('inf') for nodo in self.grafo}
        distanciasLista[origem] = 0
        queue = [(0,origem)]

        while len(queue) > 0:

            distanciaAtual, nodoAtual = queue.pop()

            if distanciaAtual > distanciasLista[nodoAtual]:
                continue

            for nodoVizinho in self.grafo[nodoAtual]:

                distanciaVizinho = self.grafo[nodoAtual][nodoVizinho]['distancia']
                distancia = distanciaAtual + distanciaVizinho

                if distancia < distanciasLista[nodoVizinho]:

                    distanciasLista[nodoVizinho] = distancia
                    queue.append((distancia,nodoVizinho))

        return distanciasLista
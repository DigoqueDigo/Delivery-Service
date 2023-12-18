import networkx as nx
import matplotlib.pyplot as plt

class Graph:

    def __init__(self):
        self.graph = nx.Graph()
        self.pathDictionary = dict()
        self.distanceDictionary = dict()


    def addNode(self,node):
        self.graph.add_node(node)


    def addEdge(self,source,destination,weigth):
        self.graph.add_edge(source,destination,distance = weigth)


    def distanceBetween(self,source,destination):
        return self.distanceDictionary[source][destination]


    def pathBetween(self,source,destination):
        return self.pathDictionary[source][destination]


    def loadDictionary(self):
        for node in self.graph:
            distanceList, pathList = self.dijkstraAll(node)
            self.distanceDictionary[node] = distanceList
            self.pathDictionary[node] = pathList


    def dijkstraAll(self,source):

        distanceList = {node: float('inf') for node in self.graph}
        pathList = {node: [] for node in self.graph}

        distanceList[source] = 0
        queue = [(0,source)]

        while len(queue) > 0:

            currentDistance, currentNode = queue.pop()

            if currentDistance > distanceList[currentNode]:
                continue

            for neighbourNode in self.graph[currentNode]:

                neighbourDisctance = self.graph[currentNode][neighbourNode]['distance']
                distance = currentDistance + neighbourDisctance

                if distance < distanceList[neighbourNode]:

                    distanceList[neighbourNode] = distance
                    queue.append((distance,neighbourNode))
                    pathList[neighbourNode] = pathList[currentNode] + [currentNode]

        for node in self.graph:
            if node != source:
                pathList[node] = pathList[node] + [node]

        return distanceList, pathList


    def plot(self):

        layout = nx.kamada_kawai_layout(self.graph)
        etiquetas = {(i, j): self.graph[i][j]['distance'] for i, j in self.graph.edges()}

        nx.draw(
            self.graph,
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
            self.graph,
            layout,
            edge_labels = etiquetas,
            font_size = 10,
            font_color = "black")

        plt.show()
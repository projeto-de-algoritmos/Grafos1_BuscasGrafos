# Scripts para plotar um grafo com a biblioteca igraph
import igraph
from igraph import *

g = Graph()
g.add_vertices(7)
g.add_edges([(0,3),(0,4),(1,0),(1,3),(1,5),(2,6),(3,4)])
print(g)
plot(g)
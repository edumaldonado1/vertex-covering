#Implementation of vertex Covering algorithm using a example from the book "Artificial Intelligence: A Modern Approach" by Russell and Norvig, page 95 (1st ed)
#Authors: Jenifer Cruz Munoz, Jose Eduardo Maldonado Oropeza
#dependence: igraph http://hal.elte.hu/~nepusz/development/igraph/tutorial/install.html

import random
import math
from igraph import *
id =-1
class Grafo():
    def __init__(self):
        id = -1

        self.n1 = Nodo("Arad", -135, 340)
        self.n2 = Nodo("Zerid", -130, 351)
        self.n3 = Nodo("Oradea", -120, 361)
        self.n4 = Nodo("Sibiu", -85, 238)
        self.n5 = Nodo("Timisoara", -135, 300)
        self.n6 = Nodo("Lugoj", -105, 220)
        self.n7 = Nodo("Mehadia", -100, 219)
        self.n8 = Nodo("Dobreta", -105, 218)
        self.n9 = Nodo("Fagaras", -40, 171)
        self.n10 = Nodo("Rimnicu Vilcea", -75, 178)
        self.n11 = Nodo("Craiova", -65, 146)
        self.n12 = Nodo("Pitesti", -35, 94)
        self.n13 = Nodo("Bucharest",0,0)
        self.n14 = Nodo("Giugiu", -10, 76)
        self.n15 = Nodo("Urziceni", 25, 77)
        self.n16 = Nodo("Hirsova", 60, 139)
        self.n17 = Nodo("Eforie", 70, 146)
        self.n18 = Nodo("Vaslui", 50, 193)
        self.n19 = Nodo("Iasi", 30, 224)
        self.n20 = Nodo("Neamt", 5, 234)

        self.ar1 = Arista(self.n1,self.n2, 75)   #Arad, Zerid
        self.ar2 = Arista(self.n1,self.n4, 140)   #Arad, Sibiu
        self.ar3 = Arista(self.n1,self.n5, 118)   #Arad, Timisoara
        self.ar4 = Arista(self.n2,self.n3, 71)   #Zerid, Oradea
        self.ar5 = Arista(self.n3,self.n4, 151)  #Oradea, Sibiu
        self.ar6 = Arista(self.n4,self.n9, 99)   #Sibiu, Fagaras
        self.ar7 = Arista(self.n4,self.n10, 80)  #Sibiu, Rimnicu Vilcea
        self.ar8 = Arista(self.n5,self.n6, 111)   #Timisoara, Lugoj
        self.ar9 = Arista(self.n6,self.n7, 70)   #Lugoj, Mehadia
        self.ar10 = Arista(self.n7,self.n8, 75)  #Mehadia, Dobreta
        self.ar11 = Arista(self.n8,self.n11, 120) #Dobreta, Craiova
        self.ar12 = Arista(self.n9,self.n13, 211) #Fagaras, Bucharest
        self.ar13 = Arista(self.n10,self.n11, 146)#Rimnicu Vilcea, Craiova
        self.ar14 = Arista(self.n10,self.n12, 97)#Rimnicu Vilcea, Pitesti
        self.ar15 = Arista(self.n11,self.n12, 138)#Craiova, Pitesti
        self.ar16 = Arista(self.n12,self.n13, 101)#Pitesti, Bucharest
        self.ar17 = Arista(self.n13,self.n14, 90)#Bucharest, Giugiu
        self.ar18 = Arista(self.n13,self.n15, 85)#Bucharest, Urziceni
        self.ar19 = Arista(self.n15,self.n16, 98)#Urziceni, Hirzova
        self.ar20 = Arista(self.n15,self.n18, 142)#Urziceni, Vaslui
        self.ar21 = Arista(self.n16,self.n17, 86)#Hirzova, Eforie
        self.ar22 = Arista(self.n18,self.n19, 92)#Vaslui, Iasi
        self.ar23 = Arista(self.n19,self.n20, 87)#Iasi, Neamtar
        
        self.nodos = [self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8, self.n9, self.n10, self.n11, self.n12, self.n13, self.n14, self.n15, self.n16, self.n17, self.n18, self.n19, self.n20]
        self.aristas = [self.ar1, self.ar2, self.ar3, self.ar4, self.ar5, self.ar6, self.ar7, self.ar8, self.ar9, self.ar10, self.ar11, self.ar12, self.ar13, self.ar14, self.ar15, self.ar16, self.ar17, self.ar18, self.ar19, self.ar20, self.ar21, self.ar22, self.ar23]
        for x in range(len(self.nodos)):
            self.nodos[x].id = id = id + 1
    def limpiarNodos(self):
        for x in range(len(self.nodos)):
            self.nodos[x].estado = 1
            self.nodos[x].distancia = 0
            self.nodos[x].padre = None            
    def vertexCover(self):
        def BuscarNodo(nodo, lista):
            for x in range(len(lista)):
                if lista[x] == nodo:
                    return True
            return False
        def foundRed(nodo):
            for x in range(len(nodo.aristas)):
                if nodo.aristas[x].getOtroNodo(nodo).estado == 2:
                    return True
            return False
        def doGBS():
            repetido = 0
            listOpen = []
            for x in range(len(self.aristas)):
                listOpen.append(self.aristas[x])
            while len(listOpen) > 0:
                c = listOpen.pop(0)
                if c.nodo1.estado == 3:
                    pnodo = c.nodo2
                else:
                    pnodo = c.nodo1
                pnodo.estado = 2
                for x in range(len(pnodo.aristas)):
                    if pnodo.aristas[x] in listOpen:
                        pnodo.aristas[x].getOtroNodo(pnodo).estado = 3
                        listOpen.remove(pnodo.aristas[x])
            return False
        doGBS()
    def plotGrafo(self):
        g = Graph(len(self.nodos)+2)
        g.vs[len(self.nodos)]["name"] = "no cubiertos"
        g.vs[len(self.nodos)]["color"] = "blue"
        g.vs[len(self.nodos)+1]["name"] = "cubiertos"
        g.vs[len(self.nodos)+1]["color"] = "red"
        g.add_edges((len(self.nodos), len(self.nodos)+1))
        for x in range(len(self.nodos)):
            g.vs[self.nodos[x].id]["name"] = self.nodos[x].nombre
            g.vs[self.nodos[x].id]["color"] = "blue"
            if self.nodos[x].estado == 2:
                g.vs[self.nodos[x].id]["color"] = "red"
                print self.nodos[x].nombre
        for x in range(len(self.aristas)):
             g.add_edges((self.aristas[x].nodo1.id , self.aristas[x].nodo2.id))
        g.vs["label"] = g.vs["name"]
        layout = g.layout("fr")
        plot(g, layout = layout)
class Arista(object):
    def __init__(self, nodo1, nodo2, peso=1):
        self.nodo1 = nodo1
        self.nodo1.aristas.append(self)
        self.nodo2 = nodo2
        self.nodo2.aristas.append(self)
        self.peso = peso
    def getOtroNodo(self, nodo):
        if self.nodo1.nombre == nodo.nombre:
            return self.nodo2
        else:
            return self.nodo1

class Nodo(object):
    """docstring for Nodo"""
    def __init__(self,name="sin nombre", x=0, y=0):
        self.id = -1
        self.nombre = name
        self.estado = 1
        self.padre = None
        self.aristas = []
        self.distancia = 0
        self.coordx = x
        self.coordy = y
        #self.H = h
    def getarista(self, nodo2):
        for x in range(len(self.aristas)):
            if self.aristas[x].getOtroNodo(self)==nodo2:
                return self.aristas[x]
    def ordenarAristas(self):
        self.aristas.sort(key=lambda arista: arista.peso)
    def calcH(self):
        xx = math.fabs(self.coordx)
        yy = math.fabs(self.coordy)
        return math.sqrt(math.pow(xx,2) + math.pow(yy,2))

grafo = Grafo()
grafo.vertexCover()
grafo.plotGrafo()

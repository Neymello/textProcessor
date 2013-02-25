class Graph(object):
    __graph = {}
    __edges = {}
    
    def getGraph(self):
        return self.__graph
    
    def addVertex(self,value):
        if(value.strip != ''):
            if (value not in self.__graph):
                self.__graph[value] = 1
            else:
                self.__graph[value] += 1
            
    def createEdge(self,nodeFrom,nodeTo):
        if((nodeFrom,nodeTo) in self.__edges):
            self.__edges[(nodeFrom,nodeTo)] += 1
        else:
            self.__edges[(nodeFrom,nodeTo)] = 1
        
    def getEdges(self):
        return self.__edges

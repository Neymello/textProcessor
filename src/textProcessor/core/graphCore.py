class Graph(object):
    '''
    Graph Object
    '''
    __graph = {}
    __edges = {}
    __words = []
    __characters = []
    
    def getGraph(self):
        return self.__graph
    
    def addVertex(self,value):
        if(value.strip != ''):
            if (value not in self.__graph):
                self.__graph[value] = 1
            else:
                self.__graph[value] += 1
            
    def createEdge(self,nodeFrom,nodeTo):
        '''
        Create an edge in the graph
        :param nodeFrom:
        :param nodeTo:
        '''
        if((nodeFrom,nodeTo) in self.__edges):
            self.__edges[(nodeFrom,nodeTo)] += 1
        else:
            self.__edges[(nodeFrom,nodeTo)] = 1
        
    def getEdges(self):
        '''
        Add edges into the graph
        '''
        return self.__edges
    
    def addWord(self,word):
        '''
        Add words into the Array of Words
        '''
        
        if(word not in self.__words):
            for c in word:
                self.addCharacter(c)
            
            self.__words.append(word)
        
    def addCharacter(self,character):
        if(character not in self.__characters):
            self.__characters.append(character)
            
    def getWord(self):
        return self.__words

    def getCharacters(self):
        return self.__characters
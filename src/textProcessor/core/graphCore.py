from warnings import catch_warnings
class Graph(object):
    '''
    Graph Object
    '''
    __graph = {}
    __edges = {}
    __words = {}
    __characters = {}
    
    def getGraph(self):
        return self.__graph
    
    def addVertex(self,value):
        import re
        if(value is not None):
            if((len(value)==1 and re.search("[a-zA-Z0-9]",value)) or len(value) > 1):
                if (value not in self.__graph):
                    self.__graph[value] = 1
                else:
                    self.__graph[value] += 1
            
    def createEdge(self,nodeFrom,nodeTo):
        import re
        '''
        Create an edge in the graph
        '''
        if(nodeFrom is not None and nodeTo is not None):
            if((len(nodeFrom)==1 and re.search("[a-zA-Z0-9]",nodeFrom)) or len(nodeFrom) > 1):
                if((len(nodeTo)==1 and re.search("[a-zA-Z0-9]",nodeTo)) or len(nodeTo) > 1):
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
        import re 
        '''
        Add words into the Array of Words
        '''
        if(word is not None):
            if((len(word)==1 and re.search("[a-zA-Z0-9]",word)) or len(word) > 1):
                if(word in self.__words):
                    self.__words[word] += 1
                else:
                    self.__words[word] = 1
        
    def addCharacter(self,character):
        if(character in self.__characters):
            self.__characters[character] += 1
        else:
            self.__characters[character] = 1
            
    def getWords(self):
        return self.__words

    def getCharacters(self):
        return self.__characters
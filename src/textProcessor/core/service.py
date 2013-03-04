class Service(object):
    
    
    __endPontuation = ['.',',',';','!','?']
    
    def populateGraph(self, text):
        from textProcessor.core.tokenCore import Token
        from textProcessor.core.graphCore import Graph
        
        tokens = Token().createTokens(text)
        graph = Graph()
        
        
        for count in range(0,len(tokens)):
            graph.addVertex(tokens[count])
            graph.addWord(tokens[count])
            
            if( count+1 < len(tokens)):
                if(tokens[count][-1:] not in (self.__endPontuation)):
                    graph.createEdge(tokens[count],tokens[count+1])

        return graph
class Service(object):
    
    __endPontuation = ['.',',',';','!','?','-']
    
    def populateGraph(self, text):
        from textProcessor.core.tokenCore import Token
        from textProcessor.core.graphCore import Graph
        
        tokens = Token().createTokens(text.lower())
        graph = Graph()
        
        
        for count in range(0,len(tokens)):
            nFrom = tokens[count]
            
            graph.addVertex(Token().removePontuation(nFrom))
            graph.addWord(Token().removePontuation(nFrom))
            
            for c in nFrom:
                graph.addCharacter(c)
            
            if( count+1 < len(tokens)):
                nTo = tokens[count+1]
                if( nFrom[-1] not in (self.__endPontuation) and nFrom[0] not in (self.__endPontuation)):
                    graph.createEdge(Token().removePontuation(nFrom),Token().removePontuation(nTo))

        return graph
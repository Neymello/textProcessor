class Token(object):
    
    def createTokens(self,text):
        lines = text.split("\n");
        tokens = []
        
        for l in lines:
            for w in l.split(" "):
                if(w.strip() != ""):
                    tokens.append(w.strip())
        
        return tokens
    
    def removePontuation(self,word):
        endPontuation = ['.',',',';','!','?','-']
        
        if(len(word)>1):
            if(word[0] in endPontuation):
                word = word[1:]
            
            if(word[-1] in endPontuation):
                word = word[:-1]
            return word
        elif(word in endPontuation):
            return ""
        else:
            return word
            
        
        
class Token(object):
    
    def createTokens(self,text):
        lines = text.split("\n");
        tokens = []
        
        for l in lines:
            for w in l.split(" "):
                if(w.strip() != ""):
                    tokens.append(w.strip())
        
        return tokens
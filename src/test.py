#! /usr/bin/python

if __name__ == '__main__':
    from textProcessor.core.service import Service 
    
    #a = Service().populateGraph("The interpreter acts as a simple calculator: you can type an expression at it and it will write the value. Expression syntax is straightforward: the operators +, -, * and / work just like in most other languages (for example, Pascal or C); parentheses can be used for grouping. For example:")
    #a = Service().populateGraph("Blest with victory and peace, may the heav'n-rescued land Praise the Power that hath made and preserved us a nation! Then conquer we must, when our cause it is just,")
    
    a = Service().populateGraph("""ney mello sampaio sadksak sdsaljda
aksjdksa
askdjsakljd
ksadjksajd ksdjklsajd sakdjsakjda skasjdkasj
ney mello sampaio""")
    
    #print(a.getGraph())
    #print(a.getEdges())
    #print(a.getNGrams())

    ngrams = a.getNGrams()
    
    #for i in ngrams:
        #print(i)
    
    #print(ngrams.keys())
    #print(ngrams.values())
    items = ngrams.values()
    sorted(items)
    #print(sorted(items))
    
    for i in sorted(ngrams.items(), key=lambda x:x[1],reverse=True)[0:3]:
        print(i[0][0])
    #print([value for key, value in items])

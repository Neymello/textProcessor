#! /usr/bin/python

if __name__ == '__main__':
    from textProcessor.core.service import Service 
    
    #a = Service().populateGraph("The interpreter acts as a simple calculator: you can type an expression at it and it will write the value. Expression syntax is straightforward: the operators +, -, * and / work just like in most other languages (for example, Pascal or C); parentheses can be used for grouping. For example:")
    a = Service().populateGraph("Blest with victory and peace, may the heav'n-rescued land Praise the Power that hath made and preserved us a nation! Then conquer we must, when our cause it is just,")
    
    print(a.getGraph())
    print(a.getEdges())

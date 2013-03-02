#! /usr/bin/python

if __name__ == '__main__':
    from textProcessor.core.service import Service 
    
    a = Service().populateGraph("The interpreter acts as a simple calculator: you can type an expression at it and it will write the value. Expression syntax is straightforward: the operators +, -, * and / work just like in most other languages (for example, Pascal or C); parentheses can be used for grouping. For example:")
    
    print(a.getGraph())
    print(a.getEdges())
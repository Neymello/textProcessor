#!/usr/bin/python
"""

CGI

"""
import cgi
import json,sys

fs = cgi.FieldStorage()

print("Content-Type: application/json\n\n")
print()

scriptPath = "/var/www/textProcessor/"

sys.path.append(scriptPath)
from textProcessor.core.service import Service

processorResult = Service().populateGraph(fs["text"].value)

edges = []
for edge in processorResult.getEdges():
    edges.append({'vFrom':edge[0],'vTo':edge[1],'weight':processorResult.getEdges()[edge]})

"""
Sort the 3-grams and create an json-liked objects array
"""
ngrams = {}
total = 0
for n in sorted(processorResult.getNGrams().items(), key=lambda x:x[1],reverse=True):
    total += processorResult.getNGrams()[n[0]]
    if(len(ngrams) < 3):
        ngrams[n[0][0]+' '+n[0][1]+' '+n[0][2]]=processorResult.getNGrams()[n[0]]
#ngrams['Others'] = total

result = {}
result['words'] = processorResult.getWords()
result['characters'] = processorResult.getCharacters()
result['nodes'] = processorResult.getGraph()
result['edges'] = edges
result['nGrams'] = ngrams

print(json.dumps(result,indent=1))
#!/usr/bin/python

import cgi
import json,sys

fs = cgi.FieldStorage()

print("Content-Type: application/json\n\n")
print()

scriptPath = "/var/www/textProcessor/"

sys.path.append(scriptPath)

from textProcessor.core.service import Service

processorResult = Service().populateGraph(fs["text"].value)

result = {}

result['graph'] = processorResult.getGraph()
edges = []

for edge in processorResult.getEdges():
    edges.append({'vFrom':edge[0],'vTo':edge[1],'weight':processorResult.getEdges()[edge]})

print(json.dumps(edges,indent=1))

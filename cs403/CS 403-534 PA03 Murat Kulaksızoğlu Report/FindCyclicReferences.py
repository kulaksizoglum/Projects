from MapReduce import *

class FindCyclicReferences(MapReduce):
    def Map(self, map_input):
        graph = {}
        for edge in map_input:
            source, target = edge
            if source not in graph:
                graph[source] = []
            graph[source].append(target)
        return graph


    def Reduce(self, reduce_input):

        cyclic_references = {}
        graph={}
        for tuples in reduce_input:
            for key,value in tuples.items():
                key= int(key)
                if key not in graph:
                    graph[key] = []
                for i in value:
                    graph[key].append(i)

        for edge in graph:
            for target in graph[edge]: 
                if target in graph :
                    if edge in graph[target]:
                        cyclic_references[(min(edge, target), max(edge, target))] = 1
        cyclic_references = {str(key): str(value) for key, value in cyclic_references.items()}
        return cyclic_references
    

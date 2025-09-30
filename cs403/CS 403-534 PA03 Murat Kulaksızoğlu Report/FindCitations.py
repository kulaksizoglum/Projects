from MapReduce import *

class FindCitations(MapReduce):
    def Map(self, map_input):
        result = []
        for edge in map_input:
            _, cited_paper_id = edge
            result.append((cited_paper_id, 1))
        return result

    def Reduce(self, reduce_input):
        result_dict = {}
        for tuples in reduce_input:
            for items in tuples:
                item= items[0]
                result_dict[item] = result_dict.get(item, 0) + 1

        return result_dict


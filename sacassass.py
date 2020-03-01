from collections import defaultdict


class Solution:
    def treeDiameter(self, edges) -> int:
        nodes = defaultdict(list)
        for i, j in edges:
            nodes[i].append(j)
            nodes[j].append(i)
        leaves = [i for i in nodes if len(nodes[i]) == 1]
        print(nodes)
        def traceback(k, node):
            if nodes[node] == [k]:
                depths[node] += [0]
                return 0
            depths[node] += (traceback(node, i) + 1 for i in nodes[node] if i != k)
            return max(depths[node])+1
        depths = defaultdict(list)
        traceback(-1, leaves[0])
        print(depths)

        print(leaves)





print(Solution().treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5]]))



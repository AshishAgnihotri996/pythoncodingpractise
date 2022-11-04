class Solution:
    def cloneGraph(self,node):
        oldToNew={}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbours:
                copy.neighbourrs.append(dfs(nei))
            return copy

        return dfs(node) if node else None

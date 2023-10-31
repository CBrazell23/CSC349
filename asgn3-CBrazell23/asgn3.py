import sys
from collections import defaultdict

archArr = []

# Idea to implement Kosaraju's algorithm from geeksforgeeks
# https://www.geeksforgeeks.org/strongly-connected-components/

class Graph:

    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.graph = defaultdict(list)

    def addEdge(self, sourceVertex, targetVertex):
        self.graph[sourceVertex].append(targetVertex)

    def depthFirstSearch(self, idx, visited_vertices, arr):
        arr = []
        visited_vertices[idx] = True
        archArr.append(idx)
        archArr.append(", ")

        if(not idx in arr):
            arr.append(int(idx))

        for i in self.graph[idx]:
            if not visited_vertices[i]:
                self.depthFirstSearch(i, visited_vertices, arr)

# DFS helper function original implementaion from geeksforgeeks
# Modified for personal use
# https://www.geeksforgeeks.org/python-program-for-depth-first-search-or-dfs-for-a-graph/
    def populateStack(self, idx, visited_vertices, stack):
        visited_vertices[idx] = True
        for i in self.graph[idx]:
            if not visited_vertices[i]:
                self.populateStack(i, visited_vertices, stack)
        stack = stack.append(idx)

# Graph Transposition function implemented from geeksforgeeks
# https://www.geeksforgeeks.org/strongly-connected-components/
    def transpose(self):
        g = Graph(self.numVertices)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def getNumSCC(self):
        numSCC = 0
        arr = []
        stack = []
        visited_vertices = [False] * (self.numVertices)

        for i in range(1, self.numVertices):
            if not visited_vertices[i]:
                self.populateStack(i, visited_vertices, stack)

        transposed = self.transpose()

        visited_vertices = [False] * (self.numVertices)

        while stack:
            num = stack.pop()
            if not visited_vertices[num]:
                numSCC += 1
                transposed.depthFirstSearch(num, visited_vertices, arr)
                archArr.append("a")
        return numSCC

numberOfVertices = 0

fileToRead = sys.argv[1]
f = open(fileToRead, "r")
numbers = []
for line in f:
  line = line[:-1]
  a, b = line.split( )
  a = int(a)
  b = int(b)
  if(a > numberOfVertices):
    numberOfVertices = a
  if(b > numberOfVertices):
    numberOfVertices = b

g = Graph(numberOfVertices + 1)

f = open(fileToRead, "r")
for line in f:
  line = line[:-1]
  a, b = line.split( )
  g.addEdge(int(a), int(b))

numStronglyConnectedComponents = g.getNumSCC()
print(numStronglyConnectedComponents, "Strongly Connected Component(s):")

newString = ""
for x in archArr:
    newString += str(x)
newString=newString[:-3]
newString = newString.replace(", a", "\n")
print(newString)
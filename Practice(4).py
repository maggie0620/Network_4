import re
import numpy as np
file1 = open('D:/Network/Network 1.txt', 'r')
net1 = file1.read()

## 4-1
# Use network 1 and treat it as directed
# Calculate its density
split1 = re.split('\n', net1)
split1.remove('')
edge1 = []
for i in range(0,len(split1)):
    num1 = re.sub('\t','',split1[i])
    edge1.append(num1)
    
mylist1 = []
for k in edge1:
    if k[0] not in mylist1:
        mylist1.append(k[0])
    if k[1] not in mylist1:
        mylist1.append(k[1])
#print(mylist1)

den = len(edge1) / len(mylist1)**2
print("Density:", den)

# Output adjacency matrix
adj_matrix = []
for start_node in mylist1:
    count = [0] * len(mylist1)
    for end_node in mylist1:
        path = start_node + end_node
        if path in edge1:
            ix = mylist1.index(end_node)
            count[ix] += 1
    adj_matrix.append(count)
print("Adjacency matrix:\n", np.array(adj_matrix))

# Output incidence matrix
inc_matrix = []
for node in mylist1:
    count = [0] * len(edge1)
    for element in edge1:
        if node in element[0]:
            ix = edge1.index(element)
            count[ix] += 1
        if node in element[1]:
            ix = edge1.index(element)
            count[ix] -= 1
    inc_matrix.append(count)
print("Incidence matrix:\n", np.array(inc_matrix))

# Find its transitive closure
from collections import defaultdict

class Transitive_closure:
    def __init__(self, nodes, edge):
        self.graph = defaultdict(list)
        self.nodes = nodes
        for k in range(0,len(edge)):
            self.graph[edge[k][0]].append(edge[k][1])
        
    def BFS(self, start, visited):
        alist = []
        alist.append(start)
        
        edge_visit = []
        while alist:
            v = alist.pop()
            for i in self.graph[v]:
                k = self.nodes.index(i)
                if visited[k] == 0:
                    visited[k] = 1
                    alist.append(i)
                    edge_visit.append(v+i)

tc = Transitive_closure(mylist1, edge1)
#print(tc.graph)
 
tc_matrix = []  
for start in mylist1:
    visited = [0] * len(tc.nodes)
    tc.BFS(start, visited)
    tc_matrix.append(visited)
print("Transitive_closure:\n", np.array(tc_matrix))

## 4-2
# Propose the algorithms with pseudocode doing:
# Adjacency matrix structure
nodes_matrix = mylist1.copy()
edges_matrix = []
for i in range(0,len(nodes_matrix)):
    for j in range(0,len(nodes_matrix)):
        if adj_matrix[i][j] == 1:
            edges_matrix.append(nodes_matrix[i] + nodes_matrix[j])
#print(edges_matrix) 
  
# Change to adjacency list stucture
class pseudo:
    def __init__(self, nodes, edges):
        self.adj_list = defaultdict(list)
        self.nodes = nodes
        for k in range(0,len(edges)):
            self.adj_list[edges[k][0]].append(edges[k][1])
    
    def BFS(self, start):
        visited = [False] * len(self.nodes)
        alist = []
        key = self.nodes.index(start)
        visited[key] = True
        alist.append(start)
        
        edge_visit = []
        while alist:
            v = alist.pop()
            for i in self.adj_list[v]:
                k = self.nodes.index(i)
                if not visited[k]:
                    visited[k] = True
                    alist.append(i)
                    edge_visit.append(v+i)
        print("BFS edge list", start, ":", edge_visit)

# Run BFS with adjacency matrix structure
pseudo_BFS = pseudo(nodes_matrix, edges_matrix)
for start in mylist1:
    pseudo_BFS.BFS(start)


# Adjacency list structure
adj_list = defaultdict(list)
for k in range(0,len(edge1)):
    adj_list[edge1[k][0]].append(edge1[k][1])
#print(adj_list)  
  
# Change to adjacency matrix stucture
class pseudo:
    def __init__(self, nodes):
        self.adj_matrix = []         
        self.nodes = nodes  
        for start_node in self.nodes:
            count = [0] * len(self.nodes)
            for end_node in self.nodes:
                if start_node + end_node in edge1:
                    ix =  self.nodes.index(end_node)
                    count[ix] += 1
            self.adj_matrix.append(count)
    
    def DFS(self, v, visited, path):
        key = self.nodes.index(v)
        visited[key] = True
        for j in range(0,len(self.nodes)):
            if self.adj_matrix[key][j] == 1 and not visited[j]:  
                path.append(v + self.nodes[j])
                self.DFS(self.nodes[j], visited, path)

# Run DFS with adjacency list structure
pseudo_DFS = pseudo(mylist1)
for start in mylist1:
    paths = []
    visited = [False] * len(mylist1)
    pseudo_DFS.DFS(start, visited, paths)
    print("DFS edge list", start,":", paths)

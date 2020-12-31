'''Finding Adjacent Nodes
A graph is a set of nodes and edges that connect those nodes.
Graph Example
There are two types of graphs; directed and undirected. In an undirected graph, the edges between nodes have no particular direction (like a two-way street) whereas in a directed graph, each edge has a direction associated with it (like a one-way street).
For two nodes in a graph to be considered adjacent to one another, there must be an edge between them. In the example given above, nodes 0 and 1 are adjacent, but nodes 0 and 2 are not.
We can encode graphs using an adjaceny matrix. An adjacency matrix for a graph with 'n' nodes is an 'n * n' matrix where the entry at row 'i' and column 'j' is a 0 if nodes 'i' and 'j' are not adjacent, and 1 if nodes 'i' and 'j' are adjacent.
For the example above, the adjacency matrix woudl be as follows:
[
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]
Your task is to determine if two nodes are adjacent in a graph when given the adjacency matrix and the two nodes.
Examples
Graph Example
Adjacency Matrix:
[
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]
Nodes 0,1 should return true.
Nodes 0,2 should return false.'''



mat=[
  [ 0, 1, 0, 0 ],
  [ 1, 0, 1, 1 ],
  [ 0, 1, 0, 1 ],
  [ 0, 1, 1, 0 ]
]

print(mat[0][1]==1)
print(mat[0][2]==1)
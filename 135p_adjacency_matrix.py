# 무한(Infinity) 정의
INF = 9999

graph_adjacency_matrix = [[0,   7,   5],
                          [7,   0, INF],
                          [5, INF,   0]]

for i in range(len(graph_adjacency_matrix)):
  print(graph_adjacency_matrix[i])

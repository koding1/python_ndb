# 인접행렬 (Adjacency_Matrix ver)

# 무한(Infinity) 정의
INF = 9999

graph_adjacency_matrix = [[0,   7,   5],
                          [7,   0, INF],
                          [5, INF,   0]]

print("인접 행렬 방식으로 구현한 그래프 자료구조")
for i in range(len(graph_adjacency_matrix)):
  print(graph_adjacency_matrix[i])
print()



# 인접리스트 (Adjacency_List ver)

# 정점이 3개 이므로 빈 list 3개를 생성하여 3행을 가진 이차원 배열을 만든다
graph_adjacency_list = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장 ( 연결된 노드, 가중치 )
graph_adjacency_list[0].append((1, 7))
graph_adjacency_list[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장 ( 연결된 노드, 가중치 )
graph_adjacency_list[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장 ( 연결된 노드, 가중치 )
graph_adjacency_list[2].append((0, 5))

print("인접 리스트 방식으로 구현한 그래프 자료구조")
for i in range(len(graph_adjacency_list)):
  print(graph_adjacency_list[i])

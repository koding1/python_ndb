from collections import deque

n, m = map(int, input().split())

maze = []
for i in range(n):
  maze.append(list(map(int, input())))

x, y = 0, 0
cost = 1
queue = deque()
queue.append([y, x])

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while queue:

  cost += 1

  tmp = queue.popleft()
  
  # 4 방향에 대한 처리
  for i in range(4):
    ny = tmp[0] + dy[i]
    nx = tmp[1] + dx[i]

    # 범위를 벗어난다면
    if (ny < 0) or (nx < 0) or (ny >= n) or (nx >= m):
      continue
    else:
      # 괴물이 있는 부분이 아니라면
      if maze[ny][nx] == 1:
        queue.append([ny, nx])
        maze[ny][nx] = maze[tmp[0]][tmp[1]] + 1

for i in range(n):
  print(maze[i])

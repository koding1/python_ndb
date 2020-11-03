# Selection sort - 선택정렬 (157p)

num_list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


for i in range(len(num_list)):
  min_index = i

  for j in range(i+1, len(num_list)):
    if num_list[min_index] > num_list[j]:
      min_index = j

  # 파이썬에서 가능한 스왑 문법
  num_list[i], num_list[min_index] = num_list[min_index], num_list[i]

print(num_list)


# Insertion Sort - 삽입정렬 (161p)

num_list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(num_list)):
  for j in range(i, 0, -1):
    if num_list[j] < num_list[j-1]:
      num_list[j], num_list[j-1] = num_list[j-1], num_list[j]
    else:
      break

print(num_list)

tree = {
    0: [1, 2],
    1: [],
    2: [3, 4],
    3: [],
    4: []
}

# BFS Tree
from collections import deque

def bfs(root):
  visited = []
  # 시작점 예약
  q = deque()
  q.append(root)
  visited.append(root)

  while q:
    # 방문
    cur_v = q.popleft()
    print(cur_v)

    # 예약
    for next_v in tree[cur_v]:
      q.append(next_v)
      visited.append(next_v)

  return visited

print(bfs(0))


class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)

def bfs(root):
  visited = []
  # 시작점 예약
  q = deque()
  q.append(root)
  visited.append(root.value)

  while q:
    # 방문
    cur_v = q.popleft()
    print(cur_v.value)

    # 예약
    if cur_v.left:
      q.append(cur_v.left)
      visited.append(cur_v.left.value)
    if cur_v.right:
      q.append(cur_v.right)
      visited.append(cur_v.right.value)

  return visited

print(bfs(root))

#DFS Tree
tree = {
    0: [1, 2],
    1: [],
    2: [3, 4],
    3: [],
    4: []
}

def dfs(cur_v):
  print(cur_v)
  for child in tree [cur_v]:
    dfs[cur_v]

  return
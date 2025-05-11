# 인접리스트

tree = {
    0: [1, 2],
    1: [],
    2: [3, 4],
    3: [],
    4: []
}

# 문제에서 트리를 input 값을 줄 때, 간선 리스트 형식
edges = [
    [0, 1], [0, 2], [2, 3], [2, 4]
]

for edge in edges:
  u, v = edge
  print(f"u:{u} -> v:{v}")
# 비어있는 트리 활용하기

tree = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: []
}

# 첫번째 방법
for u, v in edges:
  #print(f"u:{u} -> v:{v}")
  tree[u].append(v)
  tree[v].append(u)

print(tree)

# 두번째 방법
tree = {}
for u, v in edges:
  print(tree)
  if u not in tree:
    tree[u] = []
    print('비어있는 리스트 추가: ', tree)
  tree[u].append(v)
  print('노드 추가: ', tree)

# 세번째 방법
tree = {}
for u, v in edges:
  if u not in tree:
    tree[u] = []
  tree[u].append(v)
print(tree)

# 네번째 방법
from collections import defaultdict

tree = defaultdict(list)
for u, v in edges:
  tree[u].append(v)
print(tree)
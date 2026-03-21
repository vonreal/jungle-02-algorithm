# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N = int(input())
adj_dicts = defaultdict(list)

for _ in range(N-1):
    n, v = map(int, input().strip().split())
    adj_dicts[n].append(v)
    adj_dicts[v].append(n)

result = ['0'] * (N+1)
def bfs(v):
    q = deque()
    visited_set = set()

    q.append(v)
    visited_set.add(v)

    while q:
        v = q.popleft()
        for adj_node in adj_dicts[v]:
            if adj_node not in visited_set:
                result[adj_node] = str(v)
                q.append(adj_node)
                visited_set.add(adj_node)
bfs(1)

sys.stdout.write("\n".join(result[2:]))

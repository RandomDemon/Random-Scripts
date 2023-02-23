import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(q)]

friend = [set() for _ in range(n)]
for a, b in ab:
    friend[a-1].add(b-1)
    friend[b-1].add(a-1)

ans = []from collections import defaultdict

input_ = input
n, m = map(int, input_().split())
ab = [list(map(int, input_().split())) for _ in range(m)]

friend = defaultdict(set)
for a, b in ab:
    friend[a-1].add(b-1)
    friend[b-1].add(a-1)

ans = []
friends_of_1 = friend[0]
for query in range(m):
    query = list(map(int, input_().split()))
    if query[0] == 1:
        friend[query[1]-1].add(query[2]-1)
        friend[query[2]-1].add(query[1]-1)
    elif query[0] == 2:
        friend[query[1]-1].discard(query[2]-1)
        friend[query[2]-1].discard(query[1]-1)
    else:
        res = set(range(n))
        for f in friends_of_1:
            res.discard(f)
            res -= friend[f]
        ans.append(len(res))

print(*ans, sep='\n')
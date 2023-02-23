import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(q)]

friend = [set() for _ in range(n)]
for a, b in ab:
    friend[a-1].add(b-1)
    friend[b-1].add(a-1)

ans = []
for query in queries:
    if query[0] == 1:
        friend[query[1]-1].add(query[2]-1)
        friend[query[2]-1].add(query[1]-1)
    elif query[0] == 2:
        friend[queery[1]-1].discard(query[2]-1)
        friend[queery[2]-1].discard(query[1]-1)
    else:
        res = set()
        for i in range(n):
            res.add(i)
            for j in friend[1]:
                res.discard(j)
        ans.append(len(res))
print(*ans, sep='\n')

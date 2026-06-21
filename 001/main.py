N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def canCut(x):
    cnt = 0
    last = 0
    for i in range(N):
        if A[i] - last >= x and L - A[i] >= x:
            cnt += 1
            last = A[i]
    return cnt >= K

def binary_search(ok, ng):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if canCut(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(binary_search(-1, L + 1))
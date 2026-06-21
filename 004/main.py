import sys
input = sys.stdin.readline

def main(H, W, A):
    B = [[0] * W for _ in range(H)]
    BW = [0] * H
    BH = [0] * W
    for i in range(H):
        for j in range(W):
            BW[i] = BW[i] + A[i][j]
            BH[j] = BH[j] + A[i][j]
    B = [[BW[i] + BH[j] - A[i][j] for j in range(W)] for i in range(H)]
    
    for row in B:
        print(*row)

if __name__ == '__main__':
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    main(H, W, A)
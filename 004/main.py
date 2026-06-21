import sys
import numpy as np
input = sys.stdin.readline

def main(H, W, A):
    B = np.zeros((H, W), dtype=int)
    BW = np.zeros(H, dtype=int)
    BH = np.zeros(W, dtype=int)
    for i in range(H):
        for j in range(W):
            BW[i] = BW[i] + A[i][j]
            BH[j] = BH[j] + A[i][j]
    B = [int(BW[i] + BH[j] - A[i][j]) for i in range(H) for j in range(W)]
    print(B)
    
if __name__ == '__main__':
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    print("input:", A)
    main(H, W, A)
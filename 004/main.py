import sys
input = sys.stdin.readline

def main(A):
    print(A)
    pass

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    print("input:", A)
    main(A)
import itertools

N = int(input())

# 有効な括弧列かどうかを判定する関数
def is_valid(S):
    score = 0
    for i in range(N):
        if S[i] == '(':
            score += 1
        else:
            score -= 1
        if score < 0:
            return False
        
    return score == 0

# bit全探索を行う
for S in itertools.product(['(', ')'], repeat=N):
    if is_valid(S):
        print(''.join(S))
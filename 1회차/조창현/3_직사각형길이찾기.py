import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())

for t in range(T):
    a, b, c = map(int, input().split())
    rec_len = 0
    if a == c:
        rec_len = b
    elif a == b:
        rec_len = c
    else:
        rec_len = a
    print(f'#{t + 1} {rec_len}')
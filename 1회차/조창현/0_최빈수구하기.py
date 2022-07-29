import sys

sys.stdin = open("_최빈수구하기.txt")

from pprint import pprint

T = int(input())

for t in range(T):
    T_num = int(int(input()))
    score_dict = {}
    score_num = input().split()
    max_keys = []
    max_index = 0
    for i in score_num:
        score_dict[i] = 0
    #print(score_dict)
    for i in score_num:
        score_dict[i] += 1
    #pprint(score_dict)
    max_index = max(score_dict.values())
    for k, v in score_dict.items():
        if v == max_index:
            max_keys.append(k)
    print(f'#{T_num} {max(max_keys)}')
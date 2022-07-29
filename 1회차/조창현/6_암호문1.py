from pprint import pprint
import sys

sys.stdin = open("_암호문1 copy.txt")

T = int(1)

for t in range(T):
    code = {}
    code_len = int(input())
    code_list = input().split()
    for i in range(1, code_len + 1):
        code[i] = code_list[i-1]
    pprint(code)
    ord_len = int(input())
    ord = input().split('I')
    for i in range(1, ord_len + 1):
        ord_det = ord[i].split(' ')
        print(ord_det)
        print(ord_det[2])
        code_key = int(ord_det[1]) + 1
        modi_num = 3
        print(code_key)
        for j in range(int(ord_det[2])):
            key_rep = code_key + int(ord_det[2])
            print(key_rep)
            code[key_rep] = code.get(code_key)
            code_key += 1
            print(code)
        code_key = int(ord_det[1]) + 1
        modi_num = 3
        for j in range(int(ord_det[2])):
            code[code_key] = ord_det[modi_num]
            code_key += 1
            modi_num += 1
            print(code)
    pprint(code)
    # print(f'#{t + 1} ', end='')
    # for i in range(1, 11):
    #     print(code.get(i), end=' ')
    # print('')
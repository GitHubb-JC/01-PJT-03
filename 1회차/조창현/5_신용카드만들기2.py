import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())

for t in range(T):
    num_list = input()
    #print(num_list)
    num_len = 0
    filt_num = []
    for i in list(num_list):
        if i != '-':
            filt_num.append(i)
    #print(filt_num)
    if len(filt_num) == 16:
        if filt_num[0] == '3' or filt_num[0] == '4' or filt_num[0] == '5' or filt_num[0] == '6' or filt_num[0] == '9':
            print(f'#{t + 1} {1}')
        else:
            print(f'#{t + 1} {0}')
    else:
        print(f'#{t + 1} {0}')
import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())

for t in range(T):
    num_list = input().split()
    #print(num_list)
    for i in range(0, 15):
        if i % 2 == 0:
            num_list[i] = int(num_list[i]) * 2
        else:
            num_list[i] = int(num_list[i])
    #print(num_list, end=' ')
    #print('')
    num_sum = sum(num_list)
    #print(num_sum)
    if num_sum % 10 == 0:
        print(f'#{t + 1} {num_sum % 10}')
    else:
        print(f'#{t + 1} {10 - (num_sum % 10)}')
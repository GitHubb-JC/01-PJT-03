import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())

for t in range(T):
    T_num = int(input())
    earn_list = input().split()
    earn_sum = 0
    cnt = 0
    for i in earn_list:
        earn_sum += int(i)
    earn_ave = float(earn_sum / T_num)
    #print(earn_ave)
    for i in earn_list:
        if float(i) <= float(earn_ave):
            cnt += 1
    print(f'#{t + 1} {cnt}')
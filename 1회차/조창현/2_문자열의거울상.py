import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())

for t in range(T):
    word = input()
    word = word[::-1]
    mir_word = ''
    #print(word)
    for i in word:
        if i == 'b':
            mir_word += 'd'
        if i == 'd':
            mir_word += 'b'
        if i == 'q':
            mir_word += 'p'
        if i == 'p':
            mir_word += 'q'
    print(f'#{t + 1} {mir_word}')
# 스터디 해설
T=int(input())

result=''
for i in range(T):
    N, word = input().split()

    for i in word:
        for j in range(int(N)):
            result+=i
    
    result+='\n'

print(result)
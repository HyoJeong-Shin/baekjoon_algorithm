'''
# 스터디 해설

#0층 1 2 3 4 5 6 ---
#1층 1 3 6 10 15 ---
#2층 1 4 10 20 35 ---

t = int(input())

for _ in range(t):
    k = int(input()) #층
    n = int(input()) #호s
    f = [x for x in range(1,n+1)] #층의 리스트
    for i in range(k): #층수만큼 반복
        for j in range(1,n): #각층 호수만큼 반복
            f[j] += f[j-1] #아랫층 호수 사람 추가
        #print(f) #~층까지의 리스트
    print(f[-1]) #가장 마지막 수 출력
'''
'''
# 스터디 해설

#6층 12개 방 10번째 사람이라면 => 402
##print(10%6) # 하면 4가 나옴 = 층수

T = int(input())

for i in range(T):
    H,W,N = map(int,input().split()) #호텔의 층 수, 각 층의 방 수, 몇 번째 손님
    a=0 #층수
    b=0 #방호수
    if N%H == 0:
        a=H*100 #사람%층 이 0이면 그대로 층수가 나옴
        b=N//H
    else:
        a=(N%H)*100
        b=N//H + 1
    print(a + b)
'''
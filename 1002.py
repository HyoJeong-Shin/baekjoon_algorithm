'''
# 스터디 해설
import math
t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))    # 두 원 중심 사이 거리
    
    if d == 0 and r1 == r2: # 두 원이 똑같을 때
        print(-1)
        continue
        
    if d == r1+r2 or d == abs(r1-r2): #접한다
        print(1)
    elif d < abs(r1-r2) or d> r1+r2: #외부 or 내부
        print(0)
    else:
        print(2) # 두 원의 교점 2개
'''
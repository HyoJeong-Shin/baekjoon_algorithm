# 입력 : 입력의 첫 줄에는 테스트케이스의 개수 T가 주어진다. 각각의 테스트 케이스에 대해 현재 위치 x 와 목표 위치 y 가 정수로 주어지며, x는 항상 y보다 작은 값을 갖는다. (0 ≤ x < y < 231)
# 출력 : 각 테스트 케이스에 대해 x지점으로부터 y지점까지 정확히 도달하는데 필요한 최소한의 공간이동 장치 작동 회수를 출력한다.

from math import sqrt

t = int(input())
dist = []

for i in range(t):
    x, y = input().split()
    dist.append(int(y)-int(x))

for dis in dist:
    n = int(sqrt(dis))
    m = n+1
    if n == 1:
        print(dis)
    elif dis >= n*m + 1:
        print(n+m)
    elif dis >= n**2 + 1:
        print(n*2)
    else:
        print(n*2-1)
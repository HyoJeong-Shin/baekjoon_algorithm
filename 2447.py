# 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.
# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
# N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.
# 입력 : 첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.
# 출력 : 첫째 줄부터 N번째 줄까지 별을 출력한다.
''' 재귀 코드 아닌 반복문
import sys

n = int(input())

def star(i,j):
    while(i!=0):
        # 몫이 1인 경우
        if(i%3 == 1 and j%3 == 1):
            sys.stdout.write(' ')
            return None
        # 3으로 나누어서 위의 if문에 걸리면 그 부분도 빈칸 처릴
        i = i//3
        j = j//3
    sys.stdout.write('*')

for i in range(n):
    for j in range(n):
        star(i,j)
    sys.stdout.write('\n')
'''

def concat(r1, r2):     #join 연산 : "".join(list) : 리스트에서 문자열로 합쳐줌
    return [''.join(x) for x in zip(r1, r2, r1)]    
# time_list
# ['10','34','17']
# ':'.join(time_list)
# '10:34:17'

#zip 함수 : 같은 길이의 리스트를 같은 인덱스끼리 잘라서 리스트로 반환해주는 역할
# name=['a','b']
# value=[1,2]

# # for n,v in zip(name, value):
# #     print(n,v)

def star10(n):
    if n == 1:
        return ['*']
    n //= 3
    x = star10(n)
    a = concat(x, x)
    b = concat(x, [' '*n]*n)
 
    return a + b + a
 
print('\n'.join(star10(int(input()))))

# # 결과
# # a 1
# # b 2







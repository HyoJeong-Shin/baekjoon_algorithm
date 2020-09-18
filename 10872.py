# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.
# 출력 : 첫째 줄에 N!을 출력한다.

# for 문
n = int(input())
mul = 1
for i in range(1,n+1):
    mul = mul * i
print(mul)

# 재귀
def factorial(num):
    if num<=1:
        return 1
    return num*factorial(num-1)

n=int(input())
print(factorial(n))
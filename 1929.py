# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
# 출력 : 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

m, n  = map(int, input().split())

# 에라토스테네스의 체 활용
# : 일정 범위 내 수열에서 배수들을 제거해 소수만 남기는 방법 -> 체로 걸러서 소수만 남기는게 핵심
# ex) 수열 [2 3 4 5 6 7 8 9 10] 에서 2의 배수 제거 => [2 3 5 7 9] 에서 3의 배수 제거 => [2 3 5 7]

def isprime(m, n):
    n += 1      # for문 사용을 위해
    prime = [True] * n  # n개의 True가 있는 리스트 생성
    for i in range(2, int(n**0.5)+1):   # n개의 제곱근까지만 검사
        if prime[i]:    # prime[i]가 True일때
            for j in range(2*i, n, i):  # prime 내 i의 배수들을 False로 변환
                prime[j] = False
    for i in range(m, n):
        if i > 1 and prime[i] == True:  # 1 이상이면서 남은 소수들을 출력
            print(i)
            
isprime(m,n)



'''시간 초과
m, n = map(int, input().split())

for i in range(m,n+1):
    count2 = 0
    if i == 1:
        continue
    for j in range(2,i+1):
        if i % j == 0:
            count2 += 1
    if count2 == 1:
        print(i)
'''
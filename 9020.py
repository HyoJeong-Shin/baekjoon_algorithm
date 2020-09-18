# 골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
# 입력 : 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고 짝수 n이 주어진다. (4 ≤ n ≤ 10,000)
# 출력 : 각 테스트 케이스에 대해서 주어진 n의 골드바흐 파티션을 출력한다. 출력하는 소수는 작은 것부터 먼저 출력하며, 공백으로 구분한다.

# n 이하의 숫자들 중 소수 찾기
def isprime(n):
    isprime_list = []
    n += 1      # for문 사용을 위해
    prime = [True] * n  # n개의 True가 있는 리스트 생성
    for i in range(2, int(n**0.5)+1):   # n개의 제곱근까지만 검사
        if prime[i]:    # prime[i]가 True일때
            for j in range(2*i, n, i):  # prime 내 i의 배수들을 False로 변환
                prime[j] = False
    for i in range(n):
        if i > 1 and prime[i] == True:  # 1 이상이면서 남은 소수들을 출력
            isprime_list.append(i)
    return isprime_list

# n 이하의 소수들 중 합이 n : n이하의 소수들 중 합이 n이어야 하며 그 차이가 가장 작은 것을 return
def prime_sum(n):
    li = isprime(n)
    idx = max([i for i in range(len(li)) if li[i]<=n/2])    # 찾은 소수들 중 max(n/2보다 작은 수) 부터 합이 n이 되는 수
    for i in range(idx,-1,-1):
        for j in range(i,len(li)):
            if li[i]+li[j]==n:
                return [li[i],li[j]]

'''
예를 들어 n=100일 때 li의 결과는
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] 이다.
이 때, 50(=100/2)보다 작은 수 중 가장 큰 수인 47부터 합을 찾지 않고 2부터 합을 찾으면 그 결과는 3과 97이 된다.
'''

t = int(input())

for i in range(t):
    n = int(input())
    print(" ".join(map(str,prime_sum(n))))

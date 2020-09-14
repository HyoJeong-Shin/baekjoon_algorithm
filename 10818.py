# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
# 출력 : 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

# 방법 1 - 최대 최소 함수 사용
n = int(input())
a = list(map(int, input().split()))

print(min(a), max(a), sep=' ')

'''
# 방법 2 - 비교
n = int(input())
a = list(map(int, input().split()))
num_max = 0
num_min = a[0]

for i in range(n):
    if a[i] > num_max:
        num_max = a[i]
    if a[i] < num_min:
        num_min = a[i]

print(num_min, num_max, sep=' ')
'''
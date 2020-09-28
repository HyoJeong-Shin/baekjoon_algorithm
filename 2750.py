# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
# 출력 : 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

n = int(input())
asc = []

for _ in range(n):
    asc.append(int(input()))

# 버블 정렬 
for i in range(len(asc)):
    for j in range(len(asc)):
        if asc[i] < asc[j]:
            asc[i], asc[j] = asc[j], asc[i] # 위치 바꿔줌

for a in asc:
    print(a)


'''
sort 함수 사용
n = int(input())
asc = []

for i in range(n):
    asc.append(int(input()))

asc.sort()

for i in range(n):
    print(asc[i])
'''
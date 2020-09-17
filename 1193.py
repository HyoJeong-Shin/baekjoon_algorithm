# 이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.
# 출력 : 첫째 줄에 분수를 출력한다.

x = int(input())
count = 0   # 누적 
plus = 1    # 각각 묶여지는 값 (1, 2~3, 4~6, 7~10)
m = 1
n = 1

while True:
    count += plus
    if x <= count:
        y = count - x
        if plus % 2 == 0:
            print(m + (plus-1) - y,n + y, sep='/')
            break
        else:
            print(m + y,n + (plus -1) - y, sep='/')
            break
    plus +=1
        

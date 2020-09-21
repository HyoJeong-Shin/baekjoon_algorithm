# 이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.
# 출력 : 첫째 줄에 분수를 출력한다.

x = int(input())
count = 0   # 각각 묶여지는 값의 최대값 (1, 2~3, 4~6, 7~10 ...)
plus = 1    # 각각 묶여지는 값의 증가값 (1, 2, 3, 4 ...)
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
        


'''
스터디 해설 1
# 01. 배열이 하나씩 늘어남
# 02. 홀수번 배열 : 분자 감소, 분모 증가
# 03. 짝수번 배열 : 분자 증가, 분모 감소

num = int(input())
up = []   #     분모
down = [] #     분자

for i in range(1, num+1):
    if i % 2 == 0:
        # 짝수일 경우
        up += [j for j in range(1, i+1)]
        down += [j for j in range(i, 0, -1)]
    else:
        # 홀수일 경우
        down += [j for j in range(1, i+1)]
        up += [j for j in range(i, 0, -1)]

    if len(up) >= num:
        print(str(up[num-1])+'/'+str(down[num-1]))
        break

스터디 해설 2
X = int(input())

#X가 몇번째 대각선인지 찾아보자!
line = 1
line_sum = 0
pre_line_sum = 0
while True:
    pre_line_sum = line_sum
    line_sum+=line
    
    if line_sum >= X :
        break

    line+=1

X_num = X-pre_line_sum #X가 대각선 라인에서 몇번째에 위치하는지 찾아봄!
rev_X_num = line_sum+1-X

if line%2==0 :
    print(X_num,rev_X_num,sep="/") 
else :
    print(rev_X_num,X_num,sep="/")
'''
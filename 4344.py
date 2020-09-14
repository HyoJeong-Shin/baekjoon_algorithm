# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
# 입력 : 첫째 줄에는 테스트 케이스의 개수 C가 주어진다. 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 출력 : 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

c = int(input())
for i in range(c):
    n = list(map(int, input().split()))
    sum = 0
    for j in range(1,len(n)):
        sum += n[j]
    avg = sum/n[0]
    count = 0
    for j in range(1,len(n)):
        if n[j] > avg:
            count+=1
    print('%.3f%%' % ((count/(len(n)-1))*100))


'''
# 스터디 해설
C = int(input())

result_list=[]
for i in range(C):
    N = list(map(int,input().split()))
    
    avg = sum(N[1:])/N[0]#평균 구하기

    count = 0
    for j in N[1:]:
        if j>avg:
            count+=1
    
    result = round((count/N[0])*100,3)
    result_list.append(result)

for i in result_list:
    print(str("%.3f" % i)+"%")
'''
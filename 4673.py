# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
# 입력은 없다
# 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.

def d(n):
    result = n
    result = result + result//10 + result%10
    return result

list1=[]
for i in list(range(1,10001)):
  list1.append(d(i))
for j in range(1,10001):
  if j not in list1:
    print(j)



'''
# 스터디 해설
def find_selfNumber():
    n=1 #초기값
    notSelf=[] #셀프넘버가아닌 숫자 리스트 
    while n<10001:
        result=n
        for i in str(n):
            result+=int(i)
        notSelf.append(result)
        n+=1

    nums=[i for i in range(1,10001)]
    result_list= list(sorted((set(nums)-set(notSelf))))

    for i in result_list:
        print(i)

find_selfNumber()

7단계 함수 1번문제
먼저 문제에 원리를 보기 위해 10이하 숫자에서 셀프넘버가 아닌 숫자를 찾아보기 위해 1부터 연산해보면 d(1)=2, d(2)=4, d(3)=6, d(4)=8, d(5)=10 이 나온다 0~10까지 연산되서 나온 숫자인 2,4,6,8,10을 제외해보면 셀프 넘버는 1,3,5,7,9가 됨을 알 수 있다. 이 원리를 이용해서 while문을 통해 풀어보았다.

자릿수 각각 더하는 것은 n을 str로 바꾼후 for문을 돌려 n값으로 설정해놓은 result와 더하게 하였는데 더할때는 int형으로 바꿔주었다. 이렇게 하면 자기자신+각 자리수 가 구해진다. 이렇게 구해진 수는 셀프넘버가 아니므로 notSelf리스트에 추가해주었다. 이렇게 해서 10000번 구한 리스트와 1부터 10000까지 있는 리스트를 set함수를 통해 차집합 연산을 하여 결과 리스트를 구해주었다.
'''
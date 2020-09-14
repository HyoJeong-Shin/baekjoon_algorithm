# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
# 입력은 없다
# 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.

def d(n):
    result = n
    result = result + result//10 + result%10
    return result

n_list=[]
for i in list(range(1,10001)):
  list1.append(d(i))
for j in range(1,10001):
  if j not in list1:
    print(j)
    
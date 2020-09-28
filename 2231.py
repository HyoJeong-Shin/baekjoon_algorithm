n = int(input())
print_num = 0
for i in range(1, n+1):
    div_num = list(map(int, str(i)))
    sum_num = i + sum(div_num)
    if (sum_num == n):
        print_num = i
        break
print(print_num)



'''sum함수

sum(iterable)
인자 : iterable한 자료형을 받으며 numeric 해야합니다. 
즉, 리스트나 튜플 처럼 인덱스 순환 접근이 가능한 자료형이고 
내부에 숫자로만 이루어져 있어야합니다. 여기서 숫자는 정수, 실수 둘다 가능입니다

반환형 : 인자로 들어온 iterable 내부 모든 요소의 합

sum(iterable, start = 0)
이런 모양의 함수 입니다.

첫번째 인자 : iterable하고 숫자데이터가 들어간 객체, 변수

두번째 인자 : 처음으로 또 더해줄 숫자

반환 : iterable의 합 + start 값
'''
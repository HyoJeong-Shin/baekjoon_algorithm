# 스터디 해설
a = list(map(input().upper().count,map(chr,range(65,91)))) #a리스트 안에 문자가 숫자로 카운트?됨

m=max(a)#제일 많이 나온 문자(제일 높은 숫자)

if a.count(m)>1: #최댓값 숫자가 1보다 높으면 최댓값이 여러개라인 거임
    print("?")
else:
    print(chr(a.index(m)+65)) #다시 문자로 바꿔줌

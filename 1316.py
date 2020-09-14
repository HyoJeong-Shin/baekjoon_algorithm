# 스터디 예제
n = int(input())
count = 0 # 그룹 단어 아닌 애들 count
for i in range(n):
    word = input()
    s = set(word)
    word = '"' + word +'"'
    for j in s:
        if len(word.replace(j,' ').split()) > 2:
            count += 1
            break

print(n-count)
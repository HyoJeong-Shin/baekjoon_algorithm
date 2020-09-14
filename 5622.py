# 스터디 해설 1
a = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0
for i in range(len(a)):
    for j in dial:
        if a[i] in j:
            result += dial.index(j)+3
print(result)

# 스터디 해설 2
print(sum(min(ord(c)-64,25)*28//89+3 for c in input()))
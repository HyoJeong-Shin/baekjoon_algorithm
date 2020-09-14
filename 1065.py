def Han(n):
    cnt = 0
    if (n < 100):
            return n
    else:
        for i in range(100,(n+1)):
            hund = (i//100)
            ten = ((i%100)//10)
            one = ((i%100)%10)
 
            if ((hund - ten) == (ten - one)):
                cnt += 1
            return (99+cnt)
 
inp = int(input())
res = Han(inp)
print(res)


'''
# 스터디 예제
def find_Hansu(n):
    hansu=0
    for i in range(1,n+1):
        if i>=1 and i<=99:
            hansu+=1
        else:
            num=[]
            for j in str(i):
                num.append(int(j)) 

            if (num[0]-num[1]) == (num[1]-num[2]):
                hansu+=1
    print(hansu)

x=int(input())
find_Hansu(x)
'''

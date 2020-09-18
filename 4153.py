'''
# 스터디 해설
while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0 and arr[1] == 0 and arr[2] == 0:
        break
    i = arr.index(max(arr))
    if pow(arr[(i+1)%3], 2) + pow(arr[(i+2)%3], 2) == pow(arr[i], 2):
        print('right')
    else: print('wrong')
'''
import sys
 
n = int(sys.stdin.readline())
 
num_list=[]
result_list=[0 for _ in range(10001)]   #받을수의 최대값에 따라 배열을 만든다.
 
for i in range(n):
    result_list[int(sys.stdin.readline())]+=1

for i in range(len(result_list)):
    for j in range(result_list[i]):
        print(i)



'''결과는 나오나 메모리 초과 코드
def counting_sort(array, max):
    counting_array = [0]*(max+1)
    for i in array:
        counting_array[i] += 1
    for i in range(max):
        counting_array[i+1] += counting_array[i]
        
    output_array = [-1]*len(array)
    
    for i in array:
        output_array[counting_array[i] -1] = i
        counting_array[i] -= 1
    return output_array
'''

'''
https://bowbowbow.tistory.com/8
https://mong9data.tistory.com/63
'''
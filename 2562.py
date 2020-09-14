# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 입력 : 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
# 출력 : 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
'''
# 방법 1 - 비교 
num_list = [0 for i in range(9)]
num_max = 0
for i in range(9):
    n = int(input())
    num_list[i] = n
    if num_list[i] > num_max:
        num_max = num_list[i]

print(num_max, num_list.index(num_max) + 1, sep='\n')
'''

# 방법 2 - 최대 최소 함수 이용
num_list = []
for i in range(9):
    num_list.append(int(input()))

print(max(num_list), num_list.index(max(num_list))+1, sep='\n')



# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
# 입력 : 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
# 출력 : 직사각형의 네 번째 점의 좌표를 출력한다.
x_list = []
y_list = []

for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for j in range(3):
    if x_list.count(x_list[j]) == 1:    # x값이 저장된 리스트의 요소의 개수를 세어서 개수가 하나인 것을 출력함
        x = x_list[j]
    if y_list.count(y_list[j]) == 1:
        y = y_list[j]

print(x,y)
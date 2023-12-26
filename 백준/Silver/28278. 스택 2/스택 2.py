#28278
#스택2
import sys
input = sys.stdin.readline

n = int(input())
stackL = []
for _ in range(n):
    order = list(map(int, input().split()))
    if order[0] == 1:
        stackL.append(order[1])
    elif order[0] == 2:
        if stackL:
            print(stackL[-1])
            stackL.pop()
        else:
            print(-1)
    elif order[0] == 3:
        print(len(stackL))
    elif order[0] == 4:
        if stackL:
            print(0)
        else:
            print(1)
    else:
        if stackL:
            print(stackL[-1])
        else:
            print(-1)
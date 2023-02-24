"""
4
3 5 2 7 => 5 7 7 -1

4
9 5 4 8 => -1 8 8 -1
"""

n = int(input())
ans = [0] * n
A = list(map(int, input().split()))
myStack = []

for i in range(n):
    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1

result = ""

for i in range(n):
    result += str(ans[i]) + " "

print(result)

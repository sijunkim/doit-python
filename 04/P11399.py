"""
5
3 1 4 3 2 => 32
"""

N = int(input())
A = list(map(int, input().split()))
S = [0] * N

"""
1~4까지 4번
"""
for i in range(1, N):
    j = i - 1
    key = A[i]
    while A[j] > key and j >= 0:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = key

S[0] = A[0]

for i in range(1, N):
    S[i] = S[i - 1] + A[i]

sum = 0

for i in range(0, N):
    sum += S[i]

print(sum)

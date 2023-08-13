import sys

input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]

for i in range(suNo):
    prefix_sum.append(prefix_sum[i] + numbers[i])

for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s - 1])

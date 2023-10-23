"""
4 => 2333
     2339
     2393
     2399
     2939
     3119
     3137
     3733
     3739
     3793
     3797
     5939
     7193
     7331
     7333
     7393
"""

import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())


def isPrime(num):
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False
    return True


def DFS(number):
    if len(str(number)) == N:
        print(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if isPrime(number * 10 + i):
                DFS(number * 10 + i)


DFS(2)
DFS(3)
DFS(5)
DFS(7)

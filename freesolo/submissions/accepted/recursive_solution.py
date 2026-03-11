from sys import setrecursionlimit
from functools import cache

setrecursionlimit(10_000)

n = int(input())
triangle = []

for i in range(n):
	triangle.append(list(map(int, input().split())))

@cache
def triangle_solution(i: int, j: int):
	if i == n-1:
		return triangle[i][j]
	else:
		return triangle[i][j] + min(triangle_solution(i+1, j), triangle_solution(i+1, j+1))

print(triangle_solution(0, 0))
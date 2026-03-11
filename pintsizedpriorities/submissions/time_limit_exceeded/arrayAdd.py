
N, M = map(int, input().split())


m = {}
taskList = []

for i in range(N):
    inp = input().split()
    amount = int(inp[0])
    task = " ".join(inp[1:])
    m[task] = i 
    taskList.append(amount)

for _ in range(M):
    inp = input()
    if inp == "calculate":
        fst = m[input()]
        snd = m[input()]
        answer = 0
        for j in range(fst, snd+1):
            answer += taskList[j]
        print(answer) # make faster print
    else:
        inp = input().split()
        n = int(inp[0])
        task = " ".join(inp[1:])
        taskList[m[task]] += n


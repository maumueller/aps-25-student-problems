dictionary = {}

n = int(input())

for _ in range(n):
    req = input().split()
    if req[1] == "add":
        ts, _, prog, size = req

        dictionary[prog] = (int(ts), int(size))
    elif req[1] == "remove":
        _, _, prog = req

        dictionary.pop(prog)
    elif req[1] == "query":
        _, _, t1, t2 = req

        sum = 0
        for v in dictionary.values():
            if v[0] >= int(t1) and v[0] <= int(t2):
                sum += v[1]
        print(sum)
    else:
        print("Error in input")

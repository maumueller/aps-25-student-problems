prefixes = [0]
cur_prefix = 0

prog_to_ts = {}
prog_to_size = {}
ts_to_index = {}

n = int(input())

for _ in range(n):
    req = input().split()
    if req[1] == "add":
        ts, _, prog, size = req

        prog_to_ts[prog] = int(ts)              # Keeps where programs are in the list
        prog_to_size[prog] = int(size)          # Keeps size of programs, so we can remove them
        cur_prefix += int(size)                 # Current sum, which we append
        prefixes.append(cur_prefix)             
        ts_to_index[int(ts)] = len(prefixes)-1  # Set current timestamp, to latest index
    elif req[1] == "remove":
        ts, _, prog = req
        prefixes.append(cur_prefix)             # New event of 0 happened, we need to be able to query this           
        ts_to_index[int(ts)] = len(prefixes)-1


        ts = prog_to_ts[prog]

        i = ts_to_index[int(ts)]
        for x in range(i, len(prefixes)):
            prefixes[x] -= prog_to_size[prog]
        cur_prefix = prefixes[-1]               # Set next prefix to add to last value
    elif req[1] == "query":
        ts, _, t1, t2 = req
        prefixes.append(cur_prefix)             # New event of 0 happened, we need to be able to query this           
        ts_to_index[int(ts)] = len(prefixes)-1

        i1 = ts_to_index[int(t1)]
        i2 = ts_to_index[int(t2)]
        print(prefixes[i2] - prefixes[i1-1])
    else:
        print("Error in input")

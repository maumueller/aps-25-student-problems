# Problem Evaluation Report

Generated on: Wed Mar 11 10:21:31 CET 2026
Docker Image: `problemtools/icpc`

## 1. Problem: akeyboardofalltime

```text
Loading problem akeyboardofalltime
Checking config
WARNING in problem configuration: Unknown field 'uuid' provided in problem.yaml
Checking statement
Checking validators
WARNING in input format validators: No validator rejects spaces added where there already is whitespace
WARNING in input format validators: No validator rejects leading zeros added to integers
WARNING in input format validators: No validator rejects random junk added to the end of the file
Checking graders
Checking generators
WARNING in generators: Type of sample in generators.yaml must be 'directory'
WARNING in generators: Type of secret in generators.yaml must be 'directory'
Checking data
Checking submissions
   AC submission joke.py (Python 3 w/PyPy) OK: AC [CPU: 1.52s @ test case secret/15-large-09]
   Slowest AC runtime: 1.524, setting timelim to 8 secs, safety margin to 15 secs
   WA submission only_a.py (Python 3 w/PyPy) OK: WA [test case: test case sample/01, CPU: 0.21s @ test case sample/01]
   TLE submission all_paths.py (Python 3 w/PyPy) OK: TLE [test case: test case secret/07-large-01, CPU: 16.00s @ test case secret/07-large-01]
akeyboardofalltime tested: 0 errors, 6 warnings

--- STDERR ---
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested

```

## 2. Problem: bennysbiggestband

```text
Loading problem bennysbiggestband
Checking config
WARNING in problem configuration: Unknown field 'uuid' provided in problem.yaml
Checking statement
Checking validators
Checking graders
Checking generators
Checking data
Checking submissions
   AC submission incremental_updating.py (Python 3 w/PyPy) OK: AC [CPU: 12.82s @ test case secret/worst]
   Slowest AC runtime: 12.816, setting timelim to 26 secs, safety margin to 51 secs
   WA submission always_maximum.py (Python 3 w/PyPy) OK: WA [test case: test case sample/e2, CPU: 0.23s @ test case sample/e2]
   WA submission instruments_used_multiple_times.py (Python 3 w/PyPy) OK: WA [test case: test case sample/e2, CPU: 0.27s @ test case sample/e1]
   WA submission non_balancing.py (Python 3 w/PyPy) OK: WA [test case: test case sample/e2, CPU: 0.24s @ test case sample/e1]
   TLE submission binary_search.py (Python 3 w/PyPy) OK: TLE [test case: test case secret/worst, CPU: 52.05s @ test case secret/worst]
bennysbiggestband tested: 0 errors, 1 warning

--- STDERR ---
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested

```

## 3. Problem: elleninspace

```text
Loading problem elleninspace
Checking config
Checking statement
Checking validators
Checking graders
Checking generators
Checking data
Checking submissions
   AC submission correct1.py (Python 3 w/PyPy) OK: AC [CPU: 0.59s @ test case secret/13]
   Slowest AC runtime: 0.595, setting timelim to 3 secs, safety margin to 6 secs
   WA submission AICheckCentres.py (Python 3 w/PyPy) OK: WA [test case: test case secret/5, CPU: 0.51s @ test case secret/11]
   WA submission AICheckCone.py (Python 3 w/PyPy) OK: WA [test case: test case secret/2, CPU: 0.45s @ test case secret/12]
   WA submission ArctanForAngle.py (Python 3 w/PyPy) OK: WA [test case: test case secret/9, CPU: 0.62s @ test case secret/13]
   WA submission CheckCentres.py (Python 3 w/PyPy) OK: WA [test case: test case secret/5, CPU: 0.34s @ test case secret/11]
   WA submission FlatProjection.py (Python 3 w/PyPy) OK: WA [test case: test case secret/10, CPU: 0.23s @ test case sample/1]
   WA submission RoundingError.py (Python 3 w/PyPy) OK: WA [test case: test case secret/7, CPU: 0.65s @ test case secret/13]
   WA submission RoundingError2.py (Python 3 w/PyPy) OK: WA [test case: test case secret/11, CPU: 0.56s @ test case secret/11]
   WA submission StupidAngleCalc.py (Python 3 w/PyPy) OK: WA [test case: test case secret/11, CPU: 0.36s @ test case secret/11]
elleninspace tested: 0 errors, 0 warnings

--- STDERR ---
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested

```

## 4. Problem: examgaming

```text
Loading problem examgaming
Checking config
WARNING in problem configuration: Unknown field 'uuid' provided in problem.yaml
Checking statement
Checking validators
Checking graders
Checking generators
Checking data
Checking submissions
   AC submission nappy.py (Python 3 w/PyPy) OK: AC [CPU: 5.23s @ test case secret/large_onemethod]
   Slowest AC runtime: 5.233, setting timelim to 26 secs, safety margin to 52 secs
   WA submission dp.py (Python 3 w/PyPy) OK: WA [test case: test case sample/1, CPU: 0.21s @ test case sample/1]
   WA submission greedy_points.py (Python 3 w/PyPy) OK: WA [test case: test case sample/2, CPU: 0.22s @ test case sample/1]
   WA submission greedy_ratio.py (Python 3 w/PyPy) OK: WA [test case: test case sample/1, CPU: 0.22s @ test case sample/1]
   WA submission greedy_time.py (Python 3 w/PyPy) OK: WA [test case: test case sample/1, CPU: 0.25s @ test case sample/1]
   TLE submission bruteforce.py (Python 3 w/PyPy) OK: TLE [test case: test case secret/large_3methods, CPU: 53.42s @ test case secret/large_3methods]
examgaming tested: 0 errors, 1 warning

--- STDERR ---
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested

```

## 5. Problem: freesolo

```text
Loading problem freesolo
Checking config
Checking statement
Checking validators
Checking graders
Checking generators
Checking data
Checking submissions
   AC submission recursive_solution.py (Python 3 w/PyPy) OK: AC [CPU: 3.67s @ test case secret/8]
   AC submission tabular_solution.py (Python 3 w/PyPy) OK: AC [CPU: 0.68s @ test case secret/8]
   Slowest AC runtime: 3.672, setting timelim to 18 secs, safety margin to 37 secs
   WA submission greedy.py (Python 3 w/PyPy) OK: WA [test case: test case sample/2, CPU: 0.20s @ test case sample/1]
   WA submission shortest_path.py (Python 3 w/PyPy) OK: WA [test case: test case sample/4, CPU: 0.22s @ test case sample/4]
   TLE submission exhaustive_search.py (Python 3 w/PyPy) OK: TLE [test case: test case secret/0, CPU: 38.01s @ test case secret/0]
freesolo tested: 0 errors, 0 warnings

--- STDERR ---
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested

```

## 6. Problem: handin

```text
Loading problem handin
Checking config
WARNING in problem configuration: Unknown field 'problem_format_version' provided in problem.yaml
WARNING in problem configuration: Unknown field 'uuid' provided in problem.yaml
Checking statement
Checking validators
Checking graders
Checking generators
WARNING in generators: Type of sample in generators.yaml must be 'directory'
WARNING in generators: Type of secret in generators.yaml must be 'directory'
Checking data
Checking submissions
   AC submission BinaryNetworkFlow.java (Java) OK: AC [CPU: 3.97s @ test case secret/16-worst-case]
   AC submission BinaryNetworkFlow.py (Python 3 w/PyPy) OK: AC [CPU: 5.89s @ test case secret/17-worst-case-liniar]
   Slowest AC runtime: 5.892, setting timelim to 29 secs, safety margin to 59 secs
   WA submission MaxFlow.py (Python 3 w/PyPy) OK: WA [test case: test case sample/01-default, CPU: 0.19s @ test case sample/01-default]
   WA submission MaxFlowWithoutHighest.py (Python 3 w/PyPy) OK: WA [test case: test case sample/01-default, CPU: 0.19s @ test case sample/01-default]
   TLE submission LinearNetworkFlow.py (Python 3 w/PyPy) OK: TLE [test case: test case secret/17-worst-case-liniar, CPU: 60.08s @ test case secret/17-worst-case-liniar]
handin tested: 0 errors, 4 warnings

--- STDERR ---
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested

```

## 7. Problem: hungryknight

```text
Loading problem hungryknight
Checking config
Checking statement
Checking validators
WARNING in input format validators: No validator rejects spaces added where there already is whitespace
Checking graders
Checking generators
Checking data
Checking submissions
   AC submission initialsolution.py (Python 3 w/PyPy) OK: AC (11) [CPU: 5.25s @ test case secret/max]
   Slowest AC runtime: 5.248, setting timelim to 26 secs, safety margin to 52 secs
   WA submission wrongdfs.py (Python 3 w/PyPy) OK: WA [test case: test case sample/1, CPU: 0.23s @ test case sample/1]
   TLE submission nonCachingDFS.py (Python 3 w/PyPy) OK: TLE [test case: test case secret/edge_no_enemies, CPU: 53.29s @ test case secret/edge_no_enemies]
   TLE submission not_efficient.py (Python 3 w/PyPy) OK: TLE [test case: test case secret/large, CPU: 53.03s @ test case secret/large]
   TLE submission unCachedDFS.py (Python 3 w/PyPy) OK: TLE [test case: test case secret/edge_no_enemies, CPU: 53.16s @ test case secret/edge_no_enemies]
hungryknight tested: 0 errors, 1 warning

--- STDERR ---
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested

```

## 8. Problem: kattis

```text
Loading problem kattis
Checking config
Checking statement
Checking validators
Checking graders
Checking generators
Checking data
Checking submissions
   AC submission solution.py (Python 3 w/PyPy) OK: AC [CPU: 1.25s @ test case secret/2]
   Slowest AC runtime: 1.253, setting timelim to 6 secs, safety margin to 13 secs
   TLE submission sleep.py (Python 3 w/PyPy) OK: TLE [test case: test case secret/2, CPU: 14.79s @ test case secret/2]
kattis tested: 0 errors, 0 warnings

--- STDERR ---
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested

```

## 9. Problem: nixstore

```text
Loading problem nixstore
Checking config
Checking statement
Checking validators
Checking graders
Checking generators
Checking data
Checking submissions
   AC submission fenwick_tree.py (Python 3 w/PyPy) OK: AC [CPU: 1.44s @ test case secret/6]
   AC submission segment_tree.py (Python 3 w/PyPy) OK: AC [CPU: 1.44s @ test case secret/2]
   Slowest AC runtime: 1.440, setting timelim to 7 secs, safety margin to 14 secs
   WA submission sliding-window.py (Python 3 w/PyPy) OK: WA [test case: test case sample/1, CPU: 0.19s @ test case sample/1]
   WA submission total-storage.py (Python 3 w/PyPy) OK: WA [test case: test case sample/3, CPU: 0.19s @ test case sample/3]
   WA submission ts_error.py (Python 3 w/PyPy) OK: WA [test case: test case secret/1, CPU: 1.00s @ test case secret/1]
   TLE submission dict.py (Python 3 w/PyPy) OK: TLE [test case: test case secret/2, CPU: 15.05s @ test case secret/2]
   TLE submission prefix_sums.py (Python 3 w/PyPy) OK: TLE [test case: test case secret/7, CPU: 15.12s @ test case secret/7]
nixstore tested: 0 errors, 0 warnings

--- STDERR ---
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested

```

## 10. Problem: pe

```text
Loading problem pe
Checking config
Checking statement
Checking validators
Checking graders
Checking generators
Checking data
Checking submissions
   AC submission bit.c (C) OK: AC [CPU: 0.91s @ test case secret/8]
   AC submission bit.cpp (C++) OK: AC [CPU: 2.32s @ test case secret/8]
   AC submission bit.py (Python 3 w/PyPy) OK: AC [CPU: 2.46s @ test case secret/8]
   AC submission fenwick.c (C) OK: AC [CPU: 0.92s @ test case secret/8]
   AC submission fenwick.cpp (C++) OK: AC [CPU: 2.11s @ test case secret/8]
   AC submission fenwick.py (Python 3 w/PyPy) OK: AC [CPU: 2.05s @ test case secret/8]
   AC submission mergesort.c (C) OK: AC [CPU: 1.04s @ test case secret/8]
   AC submission mergesort.cpp (C++) OK: AC [CPU: 3.02s @ test case secret/8]
   AC submission mergesort.py (Python 3 w/PyPy) OK: AC [CPU: 4.67s @ test case secret/8]
   Slowest AC runtime: 4.669, setting timelim to 6 secs, safety margin to 12 secs
   WA submission hello.c (C) OK: WA [test case: test case sample/1, CPU: 0.01s @ test case sample/1]
   RTE submission rte.c (C) OK: RTE [test case: test case sample/1, CPU: 0.01s @ test case sample/1]
   TLE submission bruteforce.c (C) OK: TLE [test case: test case secret/6, CPU: 9.58s @ test case secret/6]
   TLE submission bruteforce.cpp (C++) OK: TLE [test case: test case secret/6, CPU: 9.95s @ test case secret/6]
   TLE submission bruteforce.py (Python 3 w/PyPy) OK: TLE [test case: test case secret/5, CPU: 13.00s @ test case secret/5]
pe tested: 0 errors, 0 warnings

--- STDERR ---
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested

```

## 11. Problem: pintsizedpriorities

```text
Loading problem pintsizedpriorities
Checking config
Checking statement
Checking validators
Checking graders
Checking generators
Checking data
Checking submissions
   AC submission FenwickTree.java (Java) OK: AC [CPU: 7.07s @ test case secret/randomcalcworstcaststrings]
   AC submission fenwick.py (Python 3 w/PyPy) OK: AC [CPU: 5.80s @ test case secret/randomcalcworstcaststrings]
   AC submission seqTree.py (Python 3 w/PyPy) OK: AC [CPU: 6.15s @ test case secret/randomcalcworstcaststrings]
   Slowest AC runtime: 7.069, setting timelim to 7 secs, safety margin to 8 secs
   WA submission intOverflow.java (Java) OK: WA [test case: test case secret/randomCalcUpdate, CPU: 5.52s @ test case secret/randomCalcUpdate]
   TLE submission arrayAdd.cpp (C++) OK: TLE [test case: test case secret/randomCalc, CPU: 9.00s @ test case secret/randomCalc]
   TLE submission arrayAdd.py (Python 3 w/PyPy) OK: TLE [test case: test case secret/randomCalc, CPU: 9.01s @ test case secret/randomCalc]
   TLE submission square_root.py (Python 3 w/PyPy) OK: TLE [test case: test case secret/randomCalc, CPU: 9.00s @ test case secret/randomCalc]
pintsizedpriorities tested: 0 errors, 0 warnings

--- STDERR ---
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested

```

## 12. Problem: portals

```text
Loading problem portals
Checking config
Checking statement
Checking validators
Checking graders
Checking generators
Checking data
Checking submissions
   AC submission DFS.py (Python 3 w/PyPy) OK: AC [CPU: 2.51s @ test case secret/tough]
   Slowest AC runtime: 2.513, setting timelim to 13 secs, safety margin to 25 secs
   WA submission Greedy.py (Python 3 w/PyPy) OK: WA [test case: test case secret/less_open_portals, CPU: 0.24s @ test case sample/1]
   TLE submission BFS.py (Python 3 w/PyPy) OK: TLE [test case: test case secret/tough, CPU: 26.07s @ test case secret/tough]
portals tested: 0 errors, 0 warnings

--- STDERR ---
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested

```

## 13. Problem: strikogdrik

```text
Loading problem strikogdrik
Checking config
Checking statement
Checking validators
WARNING in input format validators: No validator rejects newlines added where there already are newlines
Checking graders
Checking generators
Checking data
Checking submissions
   AC submission BFS.py (Python 3 w/PyPy) OK: AC [CPU: 3.41s @ test case secret/worst_case_BFS_Dense_1_1k]
   Slowest AC runtime: 3.408, setting timelim to 17 secs, safety margin to 34 secs
   WA submission only_output_target.py (Python 3 w/PyPy) OK: WA [test case: test case sample/1, CPU: 0.21s @ test case sample/1]
   WA submission trailing_dash.py (Python 3 w/PyPy) OK: WA [test case: test case sample/1, CPU: 0.23s @ test case sample/1]
   WA submission using_dk_path.py (Python 3 w/PyPy) OK: WA [test case: test case sample/1, CPU: 0.21s @ test case sample/1]
   WA submission using_repeated_pattern.py (Python 3 w/PyPy) OK: WA [test case: test case secret/Repeating_pattern_fail, CPU: 0.22s @ test case secret/Drunk_trap]
   WA submission wrong_unraveling_format.py (Python 3 w/PyPy) OK: WA [test case: test case sample/3, CPU: 0.22s @ test case sample/1]
strikogdrik tested: 0 errors, 1 warning

--- STDERR ---
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested

```

## 14. Problem: talisfireball

```text
Loading problem talisfireball
Checking config
Checking statement
Checking validators
Checking graders
Checking generators
Checking data
Checking submissions
   AC submission no21.py (Python 3 w/PyPy) OK: AC [CPU: 6.69s @ test case secret/FilledWithAllies2]
   Slowest AC runtime: 6.694, setting timelim to 7 secs, safety margin to 8 secs
   TLE submission good.py (Python 3 w/PyPy) OK: TLE [test case: test case secret/FilledWithAllies2, CPU: 7.19s @ test case secret/FilledWithAllies2]
   TLE submission sleep.py (Python 3 w/PyPy) OK: TLE [test case: test case secret/FilledWithAllies2, CPU: 9.04s @ test case secret/FilledWithAllies2]
talisfireball tested: 0 errors, 0 warnings

--- STDERR ---
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested

```

## 15. Problem: thegreatspacerace

```text
Loading problem thegreatspacerace
Checking config
WARNING in problem configuration: Unknown field 'uuid' provided in problem.yaml
Checking statement
Checking validators
Checking graders
Checking generators
Checking data
Checking submissions
   AC submission Solution.py (Python 3 w/PyPy) OK: AC [CPU: 0.92s @ test case secret/worst_case_full]
   Slowest AC runtime: 0.916, setting timelim to 5 secs, safety margin to 9 secs
   WA submission greedy.py (Python 3 w/PyPy) OK: WA [test case: test case sample/2, CPU: 0.22s @ test case sample/1]
   TLE submission n_squared_times_m.py (Python 3 w/PyPy) OK: TLE [test case: test case sample/3, CPU: 8.16s @ test case sample/3]
   TLE submission not_greedy_enough.py (Python 3 w/PyPy) OK: TLE [test case: test case secret/worst_case_full, CPU: 10.14s @ test case secret/worst_case_full]
thegreatspacerace tested: 0 errors, 1 warning

--- STDERR ---
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested

```


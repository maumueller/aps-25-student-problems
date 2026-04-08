# Problem Evaluation Report (problemtools/full)

Generated with: `docker run --rm -v "<problem>:/problem" problemtools/full verifyproblem /problem`

## 1. Problem: akeyboardofalltime

```text
Loading problem problem
CRITICAL Failed parsing problem.yaml. Found 1 errors:
    name: Input should be a valid string
problem tested: 1 error, 0 warnings
```

## 2. Problem: bennysbiggestband

```text
Loading problem problem
Checking config
Checking statement
Checking validators
Checking graders
Checking data
Checking submissions
   AC submission incremental_updating.py (Python 3 (w/PyPy3)) OK: AC [testcase: testcase secret/worst, CPU: 10.48s @ testcase secret/worst]
   Slowest AC runtime: 10.48, setting timelim to 21 secs, safety margin to 42 secs
   WA submission always_maximum.py (Python 3 (w/PyPy3)) OK: WA [testcase: testcase sample/e2, CPU: 0.16s @ testcase sample/e2]
   WA submission instruments_used_multiple_times.py (Python 3 (w/PyPy3)) OK: WA [testcase: testcase sample/e2, CPU: 0.21s @ testcase sample/e1]
   WA submission non_balancing.py (Python 3 (w/PyPy3)) OK: WA [testcase: testcase sample/e2, CPU: 0.21s @ testcase sample/e1]
   TLE submission binary_search.py (Python 3 (w/PyPy3)) OK: TLE [testcase: testcase secret/worst, CPU: 43.01s @ testcase secret/worst]
problem tested: 0 errors, 0 warnings
```

## 3. Problem: elleninspace

```text
Loading problem problem
CRITICAL Failed parsing problem.yaml. Found 1 errors:
    license: Input should be 'unknown', 'public domain', 'cc0', 'cc by', 'cc by-sa', 'educational' or 'permission'
problem tested: 1 error, 0 warnings
```

## 4. Problem: examgaming

```text
Loading problem problem
CRITICAL Failed parsing problem.yaml. Found 1 errors:
    limits->time_limit: Unexpected keyword argument
problem tested: 1 error, 0 warnings
```

## 5. Problem: freesolo

```text
Loading problem problem
Checking config
Checking statement
Checking validators
Checking graders
Checking data
WARNING The file /problem/data/sample/1.in contains non-standard line breaks.
WARNING The file /problem/data/sample/1.ans contains non-standard line breaks.
WARNING The file /problem/data/sample/2.in contains non-standard line breaks.
WARNING The file /problem/data/sample/2.ans contains non-standard line breaks.
WARNING The file /problem/data/sample/3.in contains non-standard line breaks.
WARNING The file /problem/data/sample/3.ans contains non-standard line breaks.
WARNING The file /problem/data/sample/4.in contains non-standard line breaks.
WARNING The file /problem/data/sample/4.ans contains non-standard line breaks.
WARNING The file /problem/data/secret/0.in contains non-standard line breaks.
WARNING The file /problem/data/secret/1.in contains non-standard line breaks.
WARNING The file /problem/data/secret/10.in contains non-standard line breaks.
WARNING The file /problem/data/secret/11.in contains non-standard line breaks.
WARNING The file /problem/data/secret/12.in contains non-standard line breaks.
WARNING The file /problem/data/secret/13.in contains non-standard line breaks.
WARNING The file /problem/data/secret/14.in contains non-standard line breaks.
WARNING The file /problem/data/secret/15.in contains non-standard line breaks.
WARNING The file /problem/data/secret/16.in contains non-standard line breaks.
WARNING The file /problem/data/secret/17.in contains non-standard line breaks.
WARNING The file /problem/data/secret/18.in contains non-standard line breaks.
WARNING The file /problem/data/secret/19.in contains non-standard line breaks.
WARNING The file /problem/data/secret/2.in contains non-standard line breaks.
WARNING The file /problem/data/secret/3.in contains non-standard line breaks.
WARNING The file /problem/data/secret/4.in contains non-standard line breaks.
WARNING The file /problem/data/secret/5.in contains non-standard line breaks.
WARNING The file /problem/data/secret/6.in contains non-standard line breaks.
WARNING The file /problem/data/secret/7.in contains non-standard line breaks.
WARNING The file /problem/data/secret/8.in contains non-standard line breaks.
WARNING The file /problem/data/secret/9.in contains non-standard line breaks.
Checking submissions
   AC submission recursive_solution.py (Python 3 (w/PyPy3)) OK: AC [testcase: testcase secret/9, CPU: 3.03s @ testcase secret/8]
   AC submission tabular_solution.py (Python 3 (w/PyPy3)) OK: AC [testcase: testcase secret/9, CPU: 0.64s @ testcase secret/8]
   Slowest AC runtime: 3.029, setting timelim to 16 secs, safety margin to 32 secs
   WA submission greedy.py (Python 3 (w/PyPy3)) OK: WA [testcase: testcase sample/2, CPU: 0.17s @ testcase sample/1]
   WA submission shortest_path.py (Python 3 (w/PyPy3)) OK: WA [testcase: testcase sample/4, CPU: 0.18s @ testcase sample/4]
   TLE submission exhaustive_search.py (Python 3 (w/PyPy3)) OK: TLE [testcase: testcase secret/0, CPU: 33.11s @ testcase secret/0]
problem tested: 0 errors, 28 warnings
```

## 6. Problem: handin

```text
Loading problem problem
Checking config
Checking statement
Checking validators
Checking graders
Checking data
Checking submissions
   AC submission BinaryNetworkFlow.java (Java) OK: AC [testcase: testcase secret/17-worst-case-liniar, CPU: 3.38s @ testcase secret/17-worst-case-liniar]
   AC submission BinaryNetworkFlow.py (Python 3 (w/PyPy3)) OK: AC [testcase: testcase secret/17-worst-case-liniar, CPU: 5.94s @ testcase secret/17-worst-case-liniar]
   Slowest AC runtime: 5.941, setting timelim to 30 secs, safety margin to 60 secs
   WA submission MaxFlow.py (Python 3 (w/PyPy3)) OK: WA [testcase: testcase sample/01-default, CPU: 0.19s @ testcase sample/01-default]
   WA submission MaxFlowWithoutHighest.py (Python 3 (w/PyPy3)) OK: WA [testcase: testcase sample/01-default, CPU: 0.19s @ testcase sample/01-default]
   TLE submission LinearNetworkFlow.py (Python 3 (w/PyPy3)) OK: TLE [testcase: testcase secret/17-worst-case-liniar, CPU: 61.11s @ testcase secret/17-worst-case-liniar]
problem tested: 0 errors, 0 warnings
```

## 7. Problem: hungryknight

```text
Loading problem problem
Checking config
Checking statement
Checking validators
WARNING No validator rejects spaces added where there already is whitespace
WARNING No validator rejects spaces added to the end of a line
Checking graders
Checking data
Checking submissions
   AC submission initialsolution.py (Python 3 (w/PyPy3)) OK: AC (11) [testcase: testcase secret/worst, CPU: 4.85s @ testcase secret/max]
   Slowest AC runtime: 4.848, setting timelim to 25 secs, safety margin to 50 secs
   WA submission wrongdfs.py (Python 3 (w/PyPy3)) OK: WA [testcase: testcase sample/1, CPU: 0.19s @ testcase sample/1]
   TLE submission nonCachingDFS.py (Python 3 (w/PyPy3)) OK: TLE [testcase: testcase secret/edge_no_enemies, CPU: 51.10s @ testcase secret/edge_no_enemies]
   TLE submission not_efficient.py (Python 3 (w/PyPy3)) OK: TLE [testcase: testcase secret/large, CPU: 51.14s @ testcase secret/large]
   TLE submission unCachedDFS.py (Python 3 (w/PyPy3)) OK: TLE [testcase: testcase secret/edge_no_enemies, CPU: 51.02s @ testcase secret/edge_no_enemies]
problem tested: 0 errors, 2 warnings
```

## 8. Problem: kattis

```text
Loading problem problem
Checking config
WARNING Missing uuid from problem.yaml. Add "uuid: a0e0e9b5-f397-455e-a0e2-7d9114a6a657" to problem.yaml.
Checking statement
Checking validators
WARNING No validator rejects spaces added to the end of a line
Checking graders
Checking data
Checking submissions
   AC submission solution.py (Python 3 (w/PyPy3)) OK: AC [testcase: testcase secret/9, CPU: 1.27s @ testcase secret/2]
   Slowest AC runtime: 1.275, setting timelim to 7 secs, safety margin to 14 secs
   TLE submission sleep.py (Python 3 (w/PyPy3)) OK: TLE [testcase: testcase secret/2, CPU: 15.02s @ testcase secret/2]
problem tested: 0 errors, 2 warnings
```

## 9. Problem: nixstore

```text
Loading problem problem
CRITICAL Failed parsing problem.yaml. Found 2 errors:
    name: Input should be a valid string
    limits->time_limit: Unexpected keyword argument
problem tested: 1 error, 0 warnings
```

## 10. Problem: pe

```text
Loading problem problem
ERROR Invalid file name 'gen tests.cpp' in problem, should match ^[a-zA-Z0-9_][a-zA-Z0-9_.-]{0,254}$
Checking config
Checking statement
Checking validators
Checking graders
Checking data
Checking submissions
   AC submission bit.c (C) OK: AC [testcase: testcase secret/9, CPU: 0.81s @ testcase secret/8]
   AC submission bit.cpp (C++) OK: AC [testcase: testcase secret/9, CPU: 2.57s @ testcase secret/8]
   AC submission bit.py (Python 3 (w/PyPy3)) OK: AC [testcase: testcase secret/9, CPU: 2.34s @ testcase secret/8]
   AC submission fenwick.c (C) OK: AC [testcase: testcase secret/9, CPU: 0.82s @ testcase secret/8]
   AC submission fenwick.cpp (C++) OK: AC [testcase: testcase secret/9, CPU: 2.52s @ testcase secret/8]
   AC submission fenwick.py (Python 3 (w/PyPy3)) OK: AC [testcase: testcase secret/9, CPU: 2.08s @ testcase secret/8]
   AC submission mergesort.c (C) OK: AC [testcase: testcase secret/9, CPU: 1.00s @ testcase secret/8]
   AC submission mergesort.cpp (C++) OK: AC [testcase: testcase secret/9, CPU: 3.14s @ testcase secret/8]
   AC submission mergesort.py (Python 3 (w/PyPy3)) OK: AC [testcase: testcase secret/9, CPU: 4.57s @ testcase secret/8]
   Slowest AC runtime: 4.575, setting timelim to 6 secs, safety margin to 12 secs
   WA submission hello.c (C) OK: WA [testcase: testcase sample/1, CPU: 0.01s @ testcase sample/1]
   RTE submission rte.c (C) OK: RTE [testcase: testcase sample/1, CPU: 0.02s @ testcase sample/1]
   TLE submission bruteforce.c (C) OK: TLE [testcase: testcase secret/6, CPU: 13.17s @ testcase secret/6]
   TLE submission bruteforce.cpp (C++) OK: TLE [testcase: testcase secret/6, CPU: 13.00s @ testcase secret/6]
   TLE submission bruteforce.py (Python 3 (w/PyPy3)) OK: TLE [testcase: testcase secret/5, CPU: 12.62s @ testcase secret/5]
problem tested: 1 error, 0 warnings
```

## 11. Problem: pintsizedpriorities

```text
Loading problem problem
CRITICAL Failed loading problem version: while parsing a block mapping
  in "/problem/problem.yaml", line 1, column 1
expected <block end>, but found '-'
  in "/problem/problem.yaml", line 2, column 1
problem tested: 1 error, 0 warnings
```

## 12. Problem: portals

```text
Loading problem problem
CRITICAL Failed parsing problem.yaml. Found 2 errors:
    limits->time_limit: Unexpected keyword argument
    limits->time_multipliers: Unexpected keyword argument
problem tested: 1 error, 0 warnings
```

## 13. Problem: strikogdrik

```text
Loading problem problem
WARNING Directory submissions/brute_force is not part of format version legacy, but part of 2023-07-draft
Checking config
Checking statement
Checking validators
WARNING No validator rejects spaces added to the end of a line
WARNING No validator rejects newlines added where there already are newlines
Checking graders
Checking data
WARNING The file /problem/data/sample/1.in contains non-standard line breaks.
WARNING The file /problem/data/sample/1.ans contains non-standard line breaks.
WARNING The file /problem/data/sample/2.in contains non-standard line breaks.
WARNING The file /problem/data/sample/2.ans contains non-standard line breaks.
WARNING The file /problem/data/sample/3.in contains non-standard line breaks.
WARNING The file /problem/data/sample/3.ans contains non-standard line breaks.
WARNING The file /problem/data/sample/4.in contains non-standard line breaks.
WARNING The file /problem/data/sample/4.ans contains non-standard line breaks.
WARNING The file /problem/data/secret/Repeating_pattern_fail.in contains non-standard line breaks.
Checking submissions
   AC submission BFS.py (Python 3 (w/PyPy3)) OK: AC [testcase: testcase secret/worst_case_BFS_linear_20k, CPU: 2.83s @ testcase secret/worst_case_BFS_Dense_1_1k]
   Slowest AC runtime: 2.829, setting timelim to 15 secs, safety margin to 30 secs
   WA submission only_output_target.py (Python 3 (w/PyPy3)) OK: WA [testcase: testcase sample/1, CPU: 0.20s @ testcase sample/1]
   WA submission trailing_dash.py (Python 3 (w/PyPy3)) OK: WA [testcase: testcase sample/1, CPU: 0.20s @ testcase sample/1]
   WA submission using_dk_path.py (Python 3 (w/PyPy3)) OK: WA [testcase: testcase sample/1, CPU: 0.22s @ testcase sample/1]
   WA submission using_repeated_pattern.py (Python 3 (w/PyPy3)) OK: WA [testcase: testcase secret/Repeating_pattern_fail, CPU: 0.20s @ testcase secret/Repeating_pattern_fail]
   WA submission wrong_unraveling_format.py (Python 3 (w/PyPy3)) OK: WA [testcase: testcase sample/3, CPU: 0.20s @ testcase sample/3]
problem tested: 0 errors, 12 warnings
```

## 14. Problem: talisfireball

```text
Loading problem problem
CRITICAL Failed parsing problem.yaml. Found 1 errors:
    limits->time: Unexpected keyword argument
problem tested: 1 error, 0 warnings
```

## 15. Problem: thegreatspacerace

```text
Loading problem problem
ERROR Invalid file name 'Input and output format.md' in problem, should match ^[a-zA-Z0-9_][a-zA-Z0-9_.-]{0,254}$
Checking config
Checking statement
Checking validators
Checking graders
Checking data
Checking submissions
   AC submission Solution.py (Python 3 (w/PyPy3)) OK: AC [testcase: testcase secret/zero, CPU: 0.79s @ testcase secret/worst_case_one_above]
   Slowest AC runtime: 0.794, setting timelim to 4 secs, safety margin to 8 secs
   WA submission greedy.py (Python 3 (w/PyPy3)) OK: WA [testcase: testcase sample/2, CPU: 0.17s @ testcase sample/2]
   TLE submission n_squared_times_m.py (Python 3 (w/PyPy3)) OK: TLE [testcase: testcase sample/3, CPU: 7.05s @ testcase sample/3]
   TLE submission not_greedy_enough.py (Python 3 (w/PyPy3)) OK: TLE [testcase: testcase secret/worst_case_full, CPU: 8.78s @ testcase secret/worst_case_full]
problem tested: 1 error, 0 warnings
```

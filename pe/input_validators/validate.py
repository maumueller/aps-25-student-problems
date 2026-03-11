from sys import stdin
import sys
import re

integer = "^(0|-?[1-9]\d*)$"

MAXN = 1000000

line = stdin.readline()
assert re.match(integer, line), "'%s' is not an integer" % line

n = int(line)
assert 1 <= n <= MAXN, "%s  not in [0, %s]" % (n, MAXN)

integers = f"\d+(?: -?\d+)" + '{' + str(n - 1) + '}'
for _ in range(2):
    line = stdin.readline()
    assert re.match(integers, line.strip()), f"'%s' is not {n} integers" % line

    numbers = list(map(int, line.split()))
    expected = list(range(1, n + 1))
    assert sorted(numbers) == expected, f"'%s' is not all integers from 1 to {n}" % line

line = stdin.readline()
assert not line, "'%s' is not empty" % line

# Nothing to report
sys.exit(42)

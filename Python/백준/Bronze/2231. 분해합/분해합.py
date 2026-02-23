import sys

line = sys.stdin.readline()
if line:
    n = int(line.strip())
    answer = 0
    for m in range(1, n + 1):
        if n == sum(map(int, str(m))) + m:
            answer = m
            break 
    print(answer)
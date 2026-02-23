n = int(input())

answer = 0
for a in range(1, 501):
    for b in range(1, a + 1):
        if a**2 == b**2 + n:
            answer += 1
print(answer)
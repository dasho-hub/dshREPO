n1 = int(input())
n2 = int(input())
n3 = int(input())
counter = 0
m1 = 0
m2 = 0
is_broken = False

for i1 in range(n1, n2 + 1):
    for i2 in range(n1, n2 + 1):
        counter += 1
        if i1 + i2 == n3:
            m1 = i1
            m2 = i2
            is_broken = True
            break
    if is_broken:
        break

if m1 + m2 == n3:
    print(f"Combination N:{counter} ({m1} + {m2} = {n3})")
else:
    print(f"{counter} combinations - neither equals {n3}")

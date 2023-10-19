n1 = int(input())
n2 = int(input())
operator = input()

if operator == "+":
    s = n1 + n2
    if s % 2 == 0:
        print(f"{n1} + {n2} = {s} - even")
    else:
        print(f"{n1} + {n2} = {s} - odd")
elif operator == "-":
    s = n1 - n2
    if s % 2 == 0:
        print(f"{n1} - {n2} = {s} - even")
    else:
        print(f"{n1} - {n2} = {s} - odd")
elif operator == "*":
    s = n1 * n2
    if s % 2 == 0:
        print(f"{n1} * {n2} = {s} - even")
    else:
        print(f"{n1} * {n2} = {s} - odd")
elif operator == "/":
    if n1 == 0 or n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        s = n1 / n2
        print(f"{n1} / {n2} = {s:.2f}")
elif operator == "%":
    if n1 == 0 or n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        s = n1 % n2
        print(f"{n1} % {n2} = {s}")
cake_a = int(input())
cake_b = int(input())

cake_pcs = cake_b * cake_a

pcs_taken = input()

while pcs_taken != "STOP":
    cake_pcs -= int(pcs_taken)
    if cake_pcs <= 0:
        break
    pcs_taken = input()

if cake_pcs <= 0:
    print(f"No more cake left! You need {abs(cake_pcs)} pieces more.")
else:
    print(f"{cake_pcs} pieces are left.")

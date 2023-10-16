budget = float(input())
extras = int(input())
single_extra_clothing = float(input())

film_decor = budget * 0.1
extras_clothing_total = single_extra_clothing * extras

if extras > 150:
    extras_clothing_total = extras_clothing_total * 0.9

total_costs = film_decor + extras_clothing_total

if total_costs > budget:
    deficit = total_costs - budget
    print("Not enough money!")
    print(f"Wingard needs {deficit:.2f} leva more.")
else:
    remainder = budget - total_costs
    print("Action!")
    print(f"Wingard starts filming with {remainder:.2f} leva left.")
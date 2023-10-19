flower_type = input()
flower_count = int(input())
budget = int(input())

price = 0
discount = 0

if flower_type == "Roses":
    price = 5
    if flower_count > 80:
        discount = 10
elif flower_type == "Dahlias":
    price = 3.80
    if flower_count > 90:
        discount = 15
elif flower_type == "Tulips":
    price = 2.80
    if flower_count > 80:
        discount = 15
elif flower_type == "Narcissus":
    price = 3
    if flower_count < 120:
        discount = -15
elif flower_type == "Gladiolus":
    price = 2.50
    if flower_count < 80:
        discount = -20
else:
    pass

final_cost = flower_count * (price - (price * discount /100))
if budget >= final_cost:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {(budget - final_cost):.2f} leva left.")
else:
    print(f"Not enough money, you need {(final_cost - budget):.2f} leva more.")
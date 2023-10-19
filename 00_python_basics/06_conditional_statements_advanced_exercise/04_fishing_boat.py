budget = int(input())
season = input()
fishermen = int(input())

discount = 0
additional_discount = 0
ship_rent = 0

if season == "Spring":
    ship_rent = 3000
elif season == "Summer" or season == "Autumn":
    ship_rent = 4200
elif season == "Winter":
    ship_rent = 2600
else:
    pass

if fishermen % 2 == 0 and season != "Autumn":
    additional_discount = 5
else:
    pass

if fishermen <= 6:
    discount = 10
elif 7 <= fishermen <= 11:
    discount = 15
elif fishermen >= 12:
    discount = 25
else:
    pass

cost = (ship_rent - (ship_rent * discount / 100))
final_cost = (cost - (cost * additional_discount / 100))

if budget >= final_cost:
    print(f"Yes! You have {(budget - final_cost):.2f} leva left.")
elif budget < final_cost:
    print(f"Not enough money! You need {(final_cost - budget):.2f} leva.")
else:
    pass

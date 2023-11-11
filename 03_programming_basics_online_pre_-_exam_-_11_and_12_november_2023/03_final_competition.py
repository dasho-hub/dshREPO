number_of_dancers = int(input())
points_given = float(input())
season = input()
place = input()
prize = 0

if place == "Bulgaria":
    prize = number_of_dancers * points_given
    if season == "summer":                                  # expenses
        prize = prize * 0.95                                #
    elif season == "winter":                                #
        prize = prize * 0.92                                # expenses
elif place == "Abroad":
    prize = (number_of_dancers * points_given) * 1.5
    if season == "summer":                                  # expenses
        prize = prize * 0.9                                 #
    elif season == "winter":                                #
        prize = prize * 0.85                                # expenses

charity_sum = prize * 0.75
money_left = prize - charity_sum
money_per_dancer = money_left / number_of_dancers

print(f"Charity - {charity_sum:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")

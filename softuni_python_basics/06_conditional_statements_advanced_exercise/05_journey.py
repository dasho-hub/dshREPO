budget = float(input())
season = input()

if budget <= 100:
    country = "Bulgaria"
    if season == "summer":
        cost = budget * 0.3
        sleep = "Camp"
    elif season == "winter":
        cost = budget * 0.7
        sleep = "Hotel"
    else:
        pass
elif 100 < budget <= 1000:
    country = "Balkans"
    if season == "summer":
        sleep = "Camp"
        cost = budget * 0.4
    elif season == "winter":
        cost = budget * 0.8
        sleep = "Hotel"
else:
    country = "Europe"
    cost = budget * 0.9
    sleep = "Hotel"

print(f"Somewhere in {country}")
print(f"{sleep} - {cost:.2f}")
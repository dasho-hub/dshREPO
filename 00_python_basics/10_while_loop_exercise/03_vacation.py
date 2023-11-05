vac_money = float(input())
current_money = float(input())

spending_days_sequence = 0
days_count = 0

while current_money < vac_money:
    action = input()
    amount = float(input())
    days_count += 1
    if action == "spend":
        spending_days_sequence += 1
        if spending_days_sequence == 5:
            print("You can't save the money.")
            print(f"{days_count}")
            break
        current_money -= amount
    elif action == "save":
        spending_days_sequence = 0
        current_money += amount
    if current_money <= 0:
        current_money = 0

if current_money >= vac_money:
    print(f"You saved the money for {days_count} days.")

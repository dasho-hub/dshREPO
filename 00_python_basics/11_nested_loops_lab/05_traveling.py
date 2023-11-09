saved_money = 0
current_money = 0
command = input()
destination = ""
budget = float(0.00)


while command != "End":
    destination = command
    budget = float(input())
    while command != "End":
        current_money = float(input())
        saved_money += current_money
        if saved_money >= budget:
            break
    print(f"Going to {destination}!")
    saved_money = 0
    command = input()
    
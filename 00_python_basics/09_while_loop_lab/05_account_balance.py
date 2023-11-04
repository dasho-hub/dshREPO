total_money = 0
deposit_amount = input()
while deposit_amount != "NoMoreMoney":
    current_sum = float(deposit_amount)
    if current_sum < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {current_sum :.2f}")
    total_money += current_sum
    deposit_amount = input()
print(f"Total: {total_money :.2f}")
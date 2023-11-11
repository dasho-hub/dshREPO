daily_allowance = float(input())
daily_income = float(input())
expenses = float(input())
present_price = float(input())

allowance = 5 * daily_allowance
income = 5 * daily_income

total_income = allowance + income
current_money = total_income - expenses

if current_money >= present_price:
    print(f"Profit: {current_money:.2f} BGN, the gift has been purchased.")
else:
    deficit = abs(present_price - current_money)
    print(f"Insufficient money: {deficit:.2f} BGN.")

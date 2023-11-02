lily_age = int(input())
washer_price = float(input())
toy_price = int(input())

bd_money_size = 0
bd_money_acc = 0
toy_count = 0

for age in range(1, lily_age + 1):
     if age % 2 == 0:
         bd_money_size += 10
         bd_money_acc += bd_money_size
         bd_money_acc -= 1
     else:
         toy_count += 1

toy_money = toy_price * toy_count
saved_money = toy_money + bd_money_acc

money_left = saved_money - washer_price

if money_left >= 0:
    print(f"Yes! {abs(money_left):.2f}")
else:
    print(f"No! {abs(money_left):.2f}")
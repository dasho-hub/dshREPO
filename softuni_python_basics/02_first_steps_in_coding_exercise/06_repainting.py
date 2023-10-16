nylon_amount = int(input())+2
paint_amount = int(input())
paint_diluent_amount = int(input())
hours_of_work = int(input())
nylon_price = 1.5
paint_price = 14.5
paint_diluent_price = 5
bags_price = 0.4
nylon_total_cost = int(nylon_amount * nylon_price)
paint_total_cost = float((paint_amount * paint_price)+(paint_amount * paint_price)*10/100)
paint_diluent_total_cost = int(paint_diluent_price * paint_diluent_amount)
total_cost_of_supplies = float(nylon_total_cost + paint_total_cost + paint_diluent_total_cost + bags_price)
hours_of_work_price = float(total_cost_of_supplies * 30/100)
total_cost = float(total_cost_of_supplies + (hours_of_work_price * hours_of_work))
print(total_cost)
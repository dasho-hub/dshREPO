pen_price = 5.8
marker_price = 7.2
detergent_liter_price = 1.2
pen_count = int(input())
marker_count = int(input())
detergent_liter_count = int(input())
discount_percent = int(input())
cost_of_supplies = (pen_count * pen_price) + (marker_count * marker_price) + (detergent_liter_count * detergent_liter_price)
discount = float((cost_of_supplies * discount_percent)/100)
print (cost_of_supplies - discount)
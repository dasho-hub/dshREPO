VIDEO_CARD_PRICE = 250
PROCESSOR_AS_MULTIPLIER = 0.35
RAM_AS_MULTIPLIER = 0.10

budget = float(input())
video_card_count = int(input())
processor_count = int(input())
ram_count = int(input())

video_card_total = video_card_count * VIDEO_CARD_PRICE
processor_price = PROCESSOR_AS_MULTIPLIER * video_card_total
ram_price = RAM_AS_MULTIPLIER * video_card_total

total_price = video_card_total + processor_count * processor_price + ram_count * ram_price

discount = 0
if video_card_count > processor_count:
    discount = 0.15

total_price_with_discount = total_price * (1 - discount)

if budget >= total_price_with_discount:
    print(f"You have {budget - total_price_with_discount :.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price_with_discount - budget :.2f} leva more!")

#
# peters_budget = float(input())
# graphic_cards = int(input())
# cpus = int(input())
# ram_pcs = int(input())
#
# graphic_cards_total_cost = graphic_cards * 250
#
# cpus_price = graphic_cards_total_cost * 0.35
# cpus_total_cost = cpus_price * cpus
#
# ram_price = graphic_cards_total_cost * 0.1
# ram_total_cost = ram_price * ram_pcs
#
# total_cost = graphic_cards_total_cost + cpus_total_cost + ram_total_cost
#
# if graphic_cards > cpus:
#     total_discount = total_cost * 0.15
# else:
#     total_discount = 0
#
# total_cost_with_discount = total_cost - total_discount
#
# if peters_budget > total_cost:
#     print (f"You have {peters_budget - total_cost_with_discount:.2f} leva left!")
# else:
#     print (f"Not enough money! You need {total_cost_with_discount - peters_budget:.2f} leva more!")
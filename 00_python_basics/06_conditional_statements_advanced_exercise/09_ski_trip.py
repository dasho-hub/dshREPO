vacation_days = int(input())
property_type = input()
evaluation = input()

room_price = 18.00
apart_price = 25.00
pres_apart_price = 35.00

if vacation_days < 10:
    if property_type == "room for one person":
        cost_for_vacation = ((vacation_days-1) * room_price) # vacation days -1 = nights
        cost_after_discount = cost_for_vacation - (cost_for_vacation * 0 / 100)
        if evaluation == "positive":
            money_given = cost_after_discount * 1.25
            print(f"{money_given:.2f}")
        else:
            money_given = cost_after_discount * 0.9
            print(f"{money_given:.2f}")
    elif property_type == "apartment":
        cost_for_vacation = ((vacation_days-1) * apart_price) # vacation days -1 = nights
        cost_after_discount = cost_for_vacation - (cost_for_vacation * 30 / 100)
        if evaluation == "positive":
            money_given = cost_after_discount * 1.25
            print(f"{money_given:.2f}")
        else:
            money_given = cost_after_discount * 0.9
            print(f"{money_given:.2f}")
    elif property_type == "president apartment":
        cost_for_vacation = ((vacation_days-1) * pres_apart_price) # vacation days -1 = nights
        cost_after_discount = cost_for_vacation - (cost_for_vacation * 10 / 100)
        if evaluation == "positive":
            money_given = cost_after_discount * 1.25
            print(f"{money_given:.2f}")
        else:
            money_given = cost_after_discount * 0.9
            print(f"{money_given:.2f}")
elif 10 <= vacation_days <= 15:
    if property_type == "room for one person":
        cost_for_vacation = ((vacation_days-1) * room_price) # vacation days -1 = nights
        cost_after_discount = cost_for_vacation - (cost_for_vacation * 0 / 100)
        if evaluation == "positive":
            money_given = cost_after_discount * 1.25
            print(f"{money_given:.2f}")
    elif property_type == "apartment":
        cost_for_vacation = ((vacation_days-1) * apart_price) # vacation days -1 = nights
        cost_after_discount = cost_for_vacation - (cost_for_vacation * 35 / 100)
        if evaluation == "positive":
            money_given = cost_after_discount * 1.25
            print(f"{money_given:.2f}")
        else:
            money_given = cost_after_discount * 0.9
            print(f"{money_given:.2f}")
    elif property_type == "president apartment":
        cost_for_vacation = ((vacation_days-1) * pres_apart_price) # vacation days -1 = nights
        cost_after_discount = cost_for_vacation - (cost_for_vacation * 15 / 100)
        if evaluation == "positive":
            money_given = cost_after_discount * 1.25
            print(f"{money_given:.2f}")
        else:
            money_given = cost_after_discount * 0.9
            print(f"{money_given:.2f}")
elif vacation_days > 15:
    if property_type == "room for one person":
        cost_for_vacation = ((vacation_days-1) * room_price) # vacation days -1 = nights
        cost_after_discount = cost_for_vacation - (cost_for_vacation * 0 / 100)
        if evaluation == "positive":
            money_given = cost_after_discount * 1.25
            print(f"{money_given:.2f}")
    elif property_type == "apartment":
        cost_for_vacation = ((vacation_days-1) * apart_price) # vacation days -1 = nights
        cost_after_discount = cost_for_vacation - (cost_for_vacation * 50 / 100)
        if evaluation == "positive":
            money_given = cost_after_discount * 1.25
            print(f"{money_given:.2f}")
        else:
            money_given = cost_after_discount * 0.9
            print(f"{money_given:.2f}")
    elif property_type == "president apartment":
        cost_for_vacation = ((vacation_days-1) * pres_apart_price) # vacation days -1 = nights
        cost_after_discount = cost_for_vacation - (cost_for_vacation * 20 / 100)
        if evaluation == "positive":
            money_given = cost_after_discount * 1.25
            print(f"{money_given:.2f}")
        else:
            money_given = cost_after_discount * 0.9
            print(f"{money_given:.2f}")
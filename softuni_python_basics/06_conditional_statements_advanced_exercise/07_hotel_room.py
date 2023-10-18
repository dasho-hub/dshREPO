month = input()
nights = int(input())

discount = 0
price = 0
total_studio_cost = 0
total_apartment_cost = 0

if month == "May" or month == "October":

    studio_cost = 50
    apart_cost = 65

    if 14 >= nights > 7:

        studio_cost = studio_cost * 0.95

        total_studio_cost = nights * studio_cost
        total_apartment_cost = nights * apart_cost

        print(f"Apartment: {total_apartment_cost:.2f} lv.")
        print(f"Studio: {total_studio_cost:.2f} lv.")

    elif nights > 14:

        studio_cost = studio_cost * 0.7
        apart_cost = apart_cost * 0.9

        total_studio_cost = nights * studio_cost
        total_apartment_cost = nights * apart_cost

        print(f"Apartment: {total_apartment_cost:.2f} lv.")
        print(f"Studio: {total_studio_cost:.2f} lv.")

    else:
        pass

elif month == "June" or month == "September":

    studio_cost = 75.20
    apart_cost = 68.70

    if nights <= 14:
        total_studio_cost = nights * studio_cost
        total_apartment_cost = nights * apart_cost

        print(f"Apartment: {total_apartment_cost:.2f} lv.")
        print(f"Studio: {total_studio_cost:.2f} lv.")

    elif nights > 14:
        studio_cost = studio_cost * 0.8
        apart_cost = apart_cost * 0.9

        total_studio_cost = nights * studio_cost
        total_apartment_cost = nights * apart_cost

        print(f"Apartment: {total_apartment_cost:.2f} lv.")
        print(f"Studio: {total_studio_cost:.2f} lv.")

elif month == "July" or month == "August":

    studio_cost = 76
    apart_cost = 77
    
    total_studio_cost = nights * studio_cost
  
    if nights > 14:
        apart_cost = (apart_cost - (apart_cost * 0.1))
        total_apartment_cost = nights * apart_cost
        print(f"Apartment: {total_apartment_cost:.2f} lv.")
    else:
        total_apartment_cost = nights * apart_cost
        print(f"Apartment: {total_apartment_cost:.2f} lv.")

    print(f"Studio: {total_studio_cost:.2f} lv.")
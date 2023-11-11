people_in_group = int(input())
nights_per_person = int(input())
bus_card_per_person = int(input())
museum_ticket_per_person = int(input())

night_price = 20
bus_card_price = 1.6
museum_ticket_price = 6

one_person_cost = ((nights_per_person * night_price) +
                   (bus_card_per_person * bus_card_price) +
                   (museum_ticket_per_person * museum_ticket_price))
all_people_cost = (one_person_cost * people_in_group)
total_cost = all_people_cost * 1.25                                         # unexpected_costs_percentage = 25%

print(f"{total_cost:.2f}")

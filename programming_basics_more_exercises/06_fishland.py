mackerel_price = float(input())
sprat_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
mussels_kg = int(input())

palamud_price = mackerel_price * 1.6
safrid_price = sprat_price * 1.8
MUSSELS_PRICE = 7.5

palamud_cost = palamud_price * palamud_kg
safrid_cost = safrid_price * safrid_kg
mussels_cost = MUSSELS_PRICE * mussels_kg

total_cost = palamud_cost + safrid_cost + mussels_cost

print(f"{total_cost:.2f}")
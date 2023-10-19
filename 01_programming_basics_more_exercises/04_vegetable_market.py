veg_kilo_price = float(input())
fru_kilo_price = float(input())
veg_kilos = float(input())
fru_kilos = float(input())

veg_cost = veg_kilos * veg_kilo_price
fru_cost = fru_kilos * fru_kilo_price

leva = veg_cost + fru_cost
euro = leva / 1.94

print (f"{euro:.2f}")
chicken_menu = 10.35
fish_menu = 12.4
vegetarian_menu = 8.15
delivery = 2.5
chicken_menu_amount = int(input())
fish_menu_amount = int(input())
vegetarian_menu_amount = int(input())
menus_total = ((chicken_menu_amount * chicken_menu) + (fish_menu_amount * fish_menu) + (vegetarian_menu_amount * vegetarian_menu))
desert_price = (menus_total*20/100)
print(menus_total + desert_price + 2.5)
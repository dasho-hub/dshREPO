pc_models = int(input())
total_rating = 0
total_sales = 0

for i in range(pc_models):
    number = str(input())
    possible_sales_str = (str(number[0]) + str(number[1]))
    possible_sales_int = int(possible_sales_str)
    rating = int(number[2])
    if rating == 2:
        rating_coef = 0
    elif rating == 3:
        rating_coef = 0.5
    elif rating == 4:
        rating_coef = 0.7
    elif rating == 5:
        rating_coef = 0.85
    elif rating == 6:
        rating_coef = 1
    total_rating += rating
    sales = possible_sales_int * rating_coef
    total_sales += sales

avg_rating = total_rating / pc_models

print(f"{total_sales:.2f}")
print(f"{avg_rating:.2f}")

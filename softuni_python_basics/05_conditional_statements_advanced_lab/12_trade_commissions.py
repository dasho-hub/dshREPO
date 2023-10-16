city = input()
sales = float(input())

commission = 0

if city == "Sofia":
    if 0 <= sales <= 500:
        commission = 5
    elif 500 < sales <= 1000:
        commission = 7
    elif 1000 < sales <= 10_000:
        commission = 8
    else:
        commission = 12
elif city == "Varna":
    if 0 <= sales <= 500:
        commission = 4.5
    elif 500 < sales <= 1000:
        commission = 7.5
    elif 1000 < sales <= 10_000:
        commission = 10
    else:
        commission = 13
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 5.5
    elif 500 < sales <= 1000:
        commission = 8
    elif 1000 < sales <= 10_000:
        commission = 12
    else:
        commission = 14.5
else:
    pass

if sales < 0 or commission <= 0:
    print("error")
else:
    print (f"{sales * (commission / 100):.2f}")
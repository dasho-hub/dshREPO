prompt_number = int(input())
if prompt_number <= 100:
    bonus = 5
elif 100 < prompt_number <= 1000:
    bonus = (prompt_number * 20 / 100)
if prompt_number > 1000:
    bonus = (prompt_number * 10 / 100)
if prompt_number % 2 == 0:
    bonus = bonus + 1
if prompt_number % 10 == 5:
    bonus = bonus + 2
print (bonus)
print (prompt_number + bonus)
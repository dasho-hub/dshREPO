number_tabs = int(input())
org_salary = int(input())

current_salary = org_salary

# Според отворения сайт в таба се налагат следните глоби:
# · "Facebook" -> 150 лв.
facebook_fine = 150
# · "Instagram" -> 100 лв.
insta_fine = 100
# · "Reddit" -> 50 лв.
reddit_fine = 50

for _ in range(number_tabs):
    tab_name = input()
    if tab_name == "Facebook":
        current_salary -= facebook_fine
    elif tab_name == "Instagram":
        current_salary -= insta_fine
    elif tab_name == "Reddit":
        current_salary -= reddit_fine
    if current_salary <= 0:
        break

if current_salary <= 0:
    print("You have lost your salary.")
else:
    print(current_salary)
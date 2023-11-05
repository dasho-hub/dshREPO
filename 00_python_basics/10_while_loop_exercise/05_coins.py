change_total = float(input())

change_total = int(change_total * 100)

number_of_coins = 0

while change_total >= 200:
    change_total -= 200
    number_of_coins += 1

# change_total is < 2 by this point

if change_total >= 100:
    change_total -= 100
    number_of_coins += 1

# change_total is < 1 by this point

if change_total >= 50:
    change_total -= 50
    number_of_coins += 1

# change_total is < 0.5 by this point

while change_total >= 20:
    change_total -= 20
    number_of_coins += 1

# change_total is < 0.2 by this point // we use 'while' because 0.2 is potentially contained twice in 0.5

if change_total >= 10:
    change_total -= 10
    number_of_coins += 1

# change_total is < 0.1 by this point

if change_total >= 5:
    change_total -= 5
    number_of_coins += 1

# change_total is < 0.05 by this point

while change_total >= 2:
    change_total -= 2
    number_of_coins += 1

# change_total is < 0.2 by this point // we use 'while' because 0.2 is potentially contained twice in 0.5

if change_total >= 1:  # we use 0.009 because of pc math
    change_total -= 1
    number_of_coins += 1

print(number_of_coins)

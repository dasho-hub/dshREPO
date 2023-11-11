sea_package_count = int(input())
mountain_package_count = int(input())
command = input()
profit_counter = 0

while command != "Stop":
    if command == "sea" and sea_package_count > 0:
        sea_package_count -= 1
        profit_counter += 680
    if command == "mountain" and mountain_package_count > 0:
        mountain_package_count -= 1
        profit_counter += 499
    if sea_package_count == 0 and mountain_package_count == 0:
        break
    command = input()

if sea_package_count == 0 and mountain_package_count == 0:
    print(f"Good job! Everything is sold.")
print(f"Profit: {profit_counter} leva.")
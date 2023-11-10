floors_count = int(input())
apart_count = int(input())

for current_floor in range(floors_count, 0, -1):
    for current_ap in range(apart_count):
        if current_floor == floors_count:
            print(f"L{current_floor}{current_ap}", end = " ")
        else:
            if current_floor % 2 == 0:
                print(f"O{current_floor}{current_ap}", end = " ")
            else:
                print(f"A{current_floor}{current_ap}", end = " ")
    print()

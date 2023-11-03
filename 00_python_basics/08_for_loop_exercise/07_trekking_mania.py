climbers_count = int(input())

musala_count = 0
monblanc_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0
total_count = 0

for _ in range(climbers_count):
    climbers_members = int(input())
    total_count += climbers_members

    if climbers_members <= 5:
        musala_count += climbers_members
    elif climbers_members <= 12:
        monblanc_count += climbers_members
    elif climbers_members <= 25:
        kilimanjaro_count += climbers_members
    elif climbers_members <= 40:
        k2_count += climbers_members
    else:
        everest_count += climbers_members

musala_percent = musala_count / total_count * 100
monblanc_percent = monblanc_count / total_count * 100
kilimanjaro_percent = kilimanjaro_count / total_count * 100
k2_percent = k2_count / total_count * 100
everest_percent = everest_count / total_count * 100

print(f"{musala_percent :.2f}%")
print(f"{monblanc_percent :.2f}%")
print(f"{kilimanjaro_percent :.2f}%")
print(f"{k2_percent :.2f}%")
print(f"{everest_percent :.2f}%")
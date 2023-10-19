# import math
#
# old_swim_record = float(input())
# distance = float(input())
# time_per_meter = float(input())
#
# slowing = 0
#
# if distance > 15:
#     slowing = int(math.floor(distance // 15))
#
# new_swim_time = (time_per_meter * distance) + (slowing * 12.5)
#
# if new_swim_time > old_swim_record:
#     print(f"No, he failed! He was {(new_swim_time - old_swim_record):.2f} seconds slower.")
# else:
#     print(f"Yes, he succeeded! The new world record is {new_swim_time:.2f} seconds.")

slowdown_in_seconds = 12.5

record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_for_a_meter = float(input())

slowdowns_count = distance_in_meters // 15

slowdown_seconds = slowdowns_count * slowdown_in_seconds

seconds_final = distance_in_meters * seconds_for_a_meter + slowdown_seconds

if seconds_final < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {seconds_final :.2f} seconds.")
else:
    print(f"No, he failed! He was {seconds_final - record_in_seconds :.2f} seconds slower.")
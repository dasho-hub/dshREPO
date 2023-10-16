hours_prompt = int(input())
minutes_prompt = int(input())

time_in_minutes = hours_prompt * 60 + minutes_prompt + 15
displayed_hours = time_in_minutes // 60
if displayed_hours == 24:
    displayed_hours = 0
displayed_minutes = time_in_minutes % 60

print(f"{displayed_hours}:{displayed_minutes:02d}")
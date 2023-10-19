num_prompt = int(input())
if num_prompt < 100:
    print("Less than 100")
elif 100 <= num_prompt <= 200:
    print("Between 100 and 200")
else:
    print("Greater than 200")
proj_type = input()
rows = int(input())
columns = int(input())

if proj_type == "Premiere":
    print(f"{(rows * columns) * 12:.2f} leva")
elif proj_type == "Normal":
    print(f"{(rows * columns) * 7.5:.2f} leva")
elif proj_type == "Discount":
    print(f"{(rows * columns) * 5:.2f} leva")
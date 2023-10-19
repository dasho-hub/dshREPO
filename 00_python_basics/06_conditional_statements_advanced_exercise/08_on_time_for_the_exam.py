exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

#Счита се, че студентът е дошъл навреме, ако е пристигнал в часа на изпита или до половин час преди това. 
# Ако е пристигнал по-рано повече от 30 минути, той е подранил. Ако е дошъл след часа на изпита, той е закъснял.

# На първия ред отпечатайте:· "Late" / "On time" / "Early".

#Ако студентът пристига с поне минута разлика от часа на изпита, отпечатайте на следващия ред:
# · "mm minutes before the start" за идване по-рано с по-малко от час;
# · "hh:mm hours before the start" за подраняване с 1 час или повече. Минутите винаги печатайте с 2 цифри, например "1:05”;
# · "mm minutes after the start" за закъснение под час;
# · "hh:mm hours after the start" за закъснение от 1 час или повече. Минутите винаги печатайте с 2 цифри, например "1:03”.

exam_minute_count = (exam_hour * 60) + exam_minute
arrival_minute_count = (arrival_hour * 60) + arrival_minute
if exam_minute_count == arrival_minute_count:
    print("On time")
else:
    if arrival_minute_count < exam_minute_count:
        early_min_amount = exam_minute_count - arrival_minute_count
        if early_min_amount < 60:
            if early_min_amount <= 30:
                print("On time")
                print(f"{early_min_amount} minutes before the start")
            else:
                print("Early")
                print(f"{early_min_amount} minutes before the start")
        else:
            print("Early")
            early_hours_amount = early_min_amount // 60
            early_min_output = early_min_amount % 60
            print(f"{early_hours_amount}:{early_min_output:02} hours before the start")

    if arrival_minute_count > exam_minute_count:
        print("Late")
        late_min_amount = arrival_minute_count - exam_minute_count
        if late_min_amount < 60:
            print(f"{late_min_amount} minutes after the start")
        else:
            late_hours_amount = late_min_amount // 60
            late_min_output = late_min_amount % 60
            print(f"{late_hours_amount}:{late_min_output:02} hours after the start")
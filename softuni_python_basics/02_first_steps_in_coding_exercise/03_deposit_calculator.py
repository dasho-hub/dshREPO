deposit_amount = float(input())
deposit_duration = int(input())
yearly_interest_rate = float(input())/100
print (deposit_amount + deposit_duration * (deposit_amount * yearly_interest_rate)/12)
hours = float(input("Enter Hours: "))
rate = float (input("Enter Rate: "))
if hours > 40:
    overtime_pay = (hours - 40) * (rate * 1.5)
    regular_pay = 40 * rate 
    pay = overtime_pay + regular_pay
else:
    pay = hours * rate 
    
print(f"Pay: {pay}")
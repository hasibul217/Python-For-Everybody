try:
    hours = float (input("Enter Hours: "))
    rate = float (input("Enter Rate: "))
except ValueError:
    print("Please enter a numerical Value, Thank You")
    exit()

pay = hours * rate 

print(f"Pay: {pay}")
    
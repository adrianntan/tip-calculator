print("Welcome to the Tip Calculator!")
total_bill = input("What was the total bill?\n$")
percent_tip = input("What percentage tip would you like to give? 10, 12, or 15?\n")
number_of_people = input("How many people to split the bill?\n")

tip = round((float(total_bill)/int(number_of_people))*(1 + (float(percent_tip)/100)), 2)

print(f"Each person has to pay: ${tip}")
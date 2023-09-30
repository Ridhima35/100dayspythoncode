print("Welcome to the tip calculator!")
bill =int(input("What was the total bill? ₹"))
tip =int(input("How much tip would you like to give? 10,15,20? "))
people = int(input("How many people to split the bill?"))
total_tip_amount =(bill * tip)/100
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = bill_per_person
print(f"if the bill was rs {bill},split b/w {people} with {tip} % tip:")
print(f"each person should pay rs {final_amount:2f}")

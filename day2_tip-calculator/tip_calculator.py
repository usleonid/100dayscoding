print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? 10, 12 or 15? ")
the_number_of_people = input("How many people to split the bill? ")

the_part_for_each = float(total_bill) * (1 + int(tip_percent) / 100) / int(the_number_of_people)

print(f"Each person should pay: ${round(the_part_for_each, 2):.2f}")

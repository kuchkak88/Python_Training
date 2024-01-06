print("Welcome to the Tip Calculator")
total_bill = float(input("What was your total bill?$ "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 15 "))
split_bill = int(input("How many people to split the bill? "))

subtotal_bill = tip_percentage / 100 * total_bill + total_bill
bill_with_tips = subtotal_bill / split_bill
final_bill = round(bill_with_tips, 2)
print(f"Each person should pay: ${final_bill}")

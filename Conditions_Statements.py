#This is a ticket purchaser
height = int(input())

if height >= 120:
    print("Good news! You are allowed to ride the rollercoaster!")
    age  = int(input())
    if age < 12:
        print("Please pay $5 for the ride")
    elif age <= 18:
        print("You should pay $7 for the ride")
    else:
        print("You pay adult price for the ride, which is $12")
else:
    print("Sorry :(. You height is not enough to rie on this rollercoaster")


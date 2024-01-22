print("Welcome to my Love Calculator")
print("The Love Calculator is calculatiing your score")
name1 = input() #What is your name?
name2 = input() #What is their name?

merged_names = name1 + name2
lower_char_names = merged_names.lower()
t = lower_char_names.count("t")
r = lower_char_names.count("r")
u = lower_char_names.count("u")
e = lower_char_names.count("e")
first_total = t + r + u + e
l = lower_char_names.count("l")
o = lower_char_names.count("o")
v = lower_char_names.count("v")
e = lower_char_names.count("e")
second_total = l + o + v + e

total = int(str(first_total) + str(second_total))
if (total < 10) or (total > 90):
    print(f"Your score is {total}, you go together like coke and mentos.")
elif (total >= 40) and (total <= 50):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
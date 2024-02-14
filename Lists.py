# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits [-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# # Your code below
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "X"
# print(f"{line1}{line2}{line3}")
# import random
#
# def get_user_choice():
#     user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
#     while user_choice not in ['rock', 'paper', 'scissors']:
#         print("Invalid choice. Please choose Rock, Paper, or Scissors.")
#         user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
#     return user_choice
#
# def get_computer_choice():
#     return random.choice(['rock', 'paper', 'scissors'])
#
# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (user_choice == 'rock' and computer_choice == 'scissors') or \
#          (user_choice == 'paper' and computer_choice == 'rock') or \
#          (user_choice == 'scissors' and computer_choice == 'paper'):
#         return "You win!"
#     else:
#         return "Computer wins!"
#
# def play_game():
#     print("Welcome to Rock, Paper, Scissors!")
#
#     while True:
#         user_choice = get_user_choice()
#         computer_choice = get_computer_choice()
#
#         print(f"You chose {user_choice}.")
#         print(f"Computer chose {computer_choice}.")
#
#         result = determine_winner(user_choice, computer_choice)
#         print(result)
#
#         play_again = input("Do you want to play again? (yes/no): ").lower()
#         if play_again != 'yes':
#             break
#
#     print("Thanks for playing!")
#
# if __name__ == "__main__":
#     play_game()
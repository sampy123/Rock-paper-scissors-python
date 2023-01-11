import random
import RPS_ASCII_Art

rps_array = [RPS_ASCII_Art.rock, RPS_ASCII_Art.paper, RPS_ASCII_Art.scissors]

user_choice = int(input(
    "Welcome to the Rock Paper Scissor game!, Type 0 for rock, 1 for paper, 2 for Scissor: "))

computer_choice = random.randint(0, 2)


if user_choice == 0:
    print(f"\nYou\n{rps_array[0]}")
    if computer_choice == 0:
        print(f"Computer\n{rps_array[0]}\nIt's a draw!")
    if computer_choice == 1:
        print(f"Computer\n{rps_array[1]}\nYou lose!")
    if computer_choice == 2:
        print(f"Computer\n{rps_array[2]}\nYou win!")
elif user_choice == 1:
    print(f"You\n{rps_array[1]}")
    if computer_choice == 0:
        print(f"Computer\n{rps_array[0]}\nYou win!")
    if computer_choice == 1:
        print(f"Computer\n{rps_array[1]}\nIt's a draw!")
    if computer_choice == 2:
        print(f"Computer\n{rps_array[2]}\nYou lose!")
elif user_choice == 2:
    print(f"You\n{rps_array[2]}")
    if computer_choice == 0:
        print(f"Computer\n{rps_array[0]}\nYou lose!")
    if computer_choice == 1:
        print(f"Computer\n{rps_array[1]}\nYou win!")
    if computer_choice == 2:
        print(f"Computer\n{rps_array[2]}\nIt's a draw!")

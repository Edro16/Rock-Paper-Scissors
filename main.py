import random

hand_position1= '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

hand_position2 = '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

hand_position3 = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

random_int = random.randint(0, 2)

match random_int:
    case 0:
        computer_hand = "rock"
    case 1:
        computer_hand = "scissors"
    case _:
        computer_hand = "paper"

print(r"""
__________               __     __________                                _________      .__                                  
\______   \ ____   ____ |  | __ \______   \_____  ______   ___________   /   _____/ ____ |__| ______ _________________  ______
 |       _//  _ \_/ ___\|  |/ /  |     ___/\__  \ \____ \_/ __ \_  __ \  \_____  \_/ ___\|  |/  ___//  ___/  _ \_  __ \/  ___/
 |    |   (  <_> )  \___|    <   |    |     / __ \|  |_> >  ___/|  | \/  /        \  \___|  |\___ \ \___ (  <_> )  | \/\___ \ 
 |____|_  /\____/ \___  >__|_ \  |____|    (____  /   __/ \___  >__|    /_______  /\___  >__/____  >____  >____/|__|  /____  >
        \/            \/     \/                 \/|__|        \/                \/     \/        \/     \/                 \/ 
""")

user_hand = input("Rock, Paper, or Scissors? - Game made by Edro\n> ").lower()

if user_hand == "paper":
    match computer_hand:
        case "paper":
            print("\nIt's a draw.")
            print(f"\nYour hand:\n{hand_position2}\n\nThe computer's hand:\n{hand_position2}")
        case "rock":
            print("\nYou've won.")
            print(f"\nYour hand:\n{hand_position2}\n\nThe computer's hand:\n{hand_position1}")
        case _:
            print("\nYou've lost.")
            print(f"\nYour hand:\n{hand_position2}\n\nThe computer's hand:\n{hand_position3}")
elif user_hand == "rock":
    match computer_hand:
        case "rock":
            print("\nIt's a draw.")
            print(f"\nYour hand:\n{hand_position1}\n\nThe computer's hand:\n{hand_position1}")
        case "scissors":
            print("\nYou've won.")
            print(f"\nYour hand:\n{hand_position1}\n\nThe computer's hand:\n{hand_position3}")
        case _:
            print("\nYou've lost.")
            print(f"\nYour hand:\n{hand_position1}\n\nThe computer's hand:\n{hand_position2}")
else:
    match computer_hand:
        case "scissors":
            print("\nIt's a draw.")
            print(f"\nYour hand:\n{hand_position3}\n\nThe computer's hand:\n{hand_position3}")
        case "paper":
            print("\nYou've won.")
            print(f"\nYour hand:\n{hand_position3}\n\nThe computer's hand:\n{hand_position2}")
        case _:
            print("\nYou've lost.")
            print(f"\nYour hand:\n{hand_position3}\n\nThe computer's hand:\n{hand_position1}")

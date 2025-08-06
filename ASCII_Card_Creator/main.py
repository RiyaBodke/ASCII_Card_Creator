import random
import os

title = """
     _    ____   ____ ___ ___    ____    _    ____  ____     ____ ____  _____    _  _____ ___  ____  
    / \  / ___| / ___|_ _|_ _|  / ___|  / \  |  _ \|  _ \   / ___|  _ \| ____|  / \|_   _/ _ \|  _ \ 
   / _ \ \___ \| |    | | | |  | |     / _ \ | |_) | | | | | |   | |_) |  _|   / _ \ | || | | | |_) |
  / ___ \ ___) | |___ | | | |  | |___ / ___ \|  _ <| |_| | | |___|  _ <| |___ / ___ \| || |_| |  _ < 
 /_/   \_\____/ \____|___|___|  \____/_/   \_\_| \_\____/   \____|_| \_\_____/_/   \_\_| \___/|_| \_\

"""
card = ""  #Variable to store card
rank_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suit_list = ["♠", "♥", "♣", "♦"]


def cls():
  os.system('cls' if os.name == 'nt' else 'clear')


def spade():
  return "♠"


def heart():
  return "♥"


def club():
  return "♣"


def diamond():
  return "♦"


def create_card(x):
  """Function to create card body"""
  n = " "
  s = " "
  h = rank_list
  for i in h:
    if i in x:
      n = i
  j = suit_list
  for k in j:
    if k in x:
      s = k
  template = ""

  #Adjusting inequal spacing
  if n == "10":
    template = f"""
   _____
  |{n}   | 
  |     |
  |  {s}  |
  |     |
  |___{n}|

    """
  else:
    template = f"""
   _____
  |{n}    | 
  |     |
  |  {s}  |
  |     |
  |____{n}|

    """
  return template


def ask_suit():
  """Function to ask user for suit"""
  c = ""
  suit_select = {1: spade(), 2: heart(), 3: club(), 4: diamond()}

  tsuit = True
  while (tsuit):
    suit = int(
        input(
            "\nSelect a suit : \n1. Spade   (♠) \n2. Heart   (♥)\n3. Club    (♣) \n4. Diamond (♦) \n\nUser : "
        ))
    if (suit > 4 or suit < 1):
      print("\nEnter a valid choice")
    else:
      tsuit = False
      c = suit_select[suit]
      return c


def full_deck(ds):
  """Function to generate deck of suit (ds)"""
  for i in rank_list:
    print(create_card(ds + i))


def single_card(s):
  """Function to generate single card with suit s"""
  trank = True
  while (trank):
    rank = input(
        "\nEnter the rank of card : \n1. (A) for Ace \n2. (J) for Jack \n3. (Q) for Queen \n4. (K) for King\n5. Number 2-10 \n\nUser : "
    )
    rank.upper()
    if (rank not in rank_list):
      print("\nEnter a valid rank")
    else:
      trank = False
      s += rank
      return (create_card(s))


def random_card():
  """Function to generate a random card"""
  i = random.choice(suit_list)
  j = random.choice(rank_list)
  return print(create_card(i + j))


def main():
  """Main function"""
  print(title)

  tchoice = True
  while (tchoice):
    choice = int(
        input(
            "\nWhat do you want? \n1. Full Deck \n2. Single Card \n3. Random Card \n\nUser : "
        ))
    if (choice == 1):
      tchoice = False
      deck_suit = ask_suit()
      full_deck(deck_suit)

    elif (choice == 2):
      tchoice = False
      single_card_suit = ask_suit()
      final_card = single_card(single_card_suit)
      print(final_card)

    elif (choice == 3):
      tchoice = False
      random_card()

    else:
      print("Enter a valid choice")


program = True
while (program):
  main()
  cont = input("Do you want to continue? (Y/N) : ")
  cont = cont.upper()
  if (cont == "Y" or cont == "YES"):
    program = True
    cls()
  else:
    program = False
    print("Bye")

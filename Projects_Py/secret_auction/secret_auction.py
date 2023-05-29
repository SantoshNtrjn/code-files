import os
import art
print(art.logo)

def highest_bid(dict):
  max_val = 0
  for key in dict:
    if dict[key] > max_val:
      max_val = dict[key]
      winner = key
  print(f'The winner is {winner} with a bid of ${max_val}')
  
start = True
bidders_dict = {}
while start:
  user_name = input("What is your name?: ")
  bid_amount = int(input("What is your bid?: $"))
  bidders_dict[user_name] = bid_amount
  is_there_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if is_there_bidders == "yes":
    os.system('cls')
  elif is_there_bidders == "no":
    os.system('cls')
    highest_bid(dict = bidders_dict)
    start = False
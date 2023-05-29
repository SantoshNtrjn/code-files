import math
import os
from art import logo

def add(n1,n2):
  return n1 + n2
def sub(n1,n2):
  return n1 - n2
def mul(n1,n2):
  return n1 * n2
def div(n1,n2):
  return n1 / n2
def exp(n1,n2):
  return math.pow(n1,n2)


def calculator():
  print(logo)
  operations = {
  "+": add,
  "-": sub ,
  "*": mul,
  "/": div,
  "**": exp,

  }
  num1 = float(input("What is the first number?: "))
  for symbols in operations:
    print(symbols)
  operation_symbol = input("pick an operation from the line above: ")
  num2 = float(input("What is the second number?: "))
  function = operations[operation_symbol]
  answer = function(n1 = num1,n2 = num2)
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  run = True
  while run:
    condition = input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or 'Q' to quit: ").lower()
    if condition == "y":
      operation_symbol = input("Pick an operation: ")
      next_num = float(input("What's the next number?: "))
      function = operations[operation_symbol]
      latest_answer = function(n1 = answer,n2 = next_num)
      print(f"{answer} {operation_symbol} {next_num} = {latest_answer}")
      answer = latest_answer
    elif condition == "n":
      run = False
      os.system('cls')
      calculator()
    else:
      run = False
      
calculator()
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def make_coffee(coffee, cash):
     if cash >= MENU[coffee]["cost"]:
         for items in MENU[coffee]["ingredients"]:
            resources[items] -= MENU[coffee]["ingredients"][items]
            cash -= MENU[coffee]["cost"]
            global profit
            profit += MENU[coffee]["cost"]
            print(f"\nHere's your ${round(cash, 2)} in change.")
            return f"\nHere's your {coffee} ☕. Enjoy!\n"
     else:
         return "\nMoney insufficient to process.\n"
                

def calc_coins():
    print("Please insert coins.\n")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    cash_in = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
    return cash_in

def resources_check(coffee_type):
    for items in coffee_type["ingredients"]:
        if resources[items] >= coffee_type["ingredients"][items]:
            return True
        else:
            print("Sorry, Resources are insufficient!\n")
            return False

run = True

while(run):
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    
    if user_input.lower() == "report":
        print(f'water : {resources["water"]}ml')
        print(f'milk : {resources["milk"]}ml')
        print(f'coffee : {resources["coffee"]}g')
        print(f'money : ${profit}')

        print('\n')
    
    elif user_input.lower() == "menu":
        for items in MENU:
            print(f"{items} : ${MENU[items]['cost']}")
        print("\n")

    elif user_input.lower() == "off":
        run = False
    
    else:
        if user_input.lower() in ["espresso","latte","cappuccino"]: 
            resources_sufficient = resources_check(MENU[user_input])
            if(resources_sufficient):
                cash_in = calc_coins()
                made_coffee = make_coffee(user_input, cash_in)
                print(made_coffee)
        else:
            print("\nInvalid Item! Try again.\n")
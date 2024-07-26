from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

run = True
items = Menu()
maker = CoffeeMaker()
money_slot = MoneyMachine()

while(run):
    user_input = input(f"What would you like? ({items.get_items()}): ")
    if user_input.lower() == "report":
        maker.report()
        money_slot.report()
    elif user_input.lower() == "off":
        run = False
    else:
        if items.find_drink(user_input):
            coffee_type = items.find_drink(user_input)
            if maker.is_resource_sufficient(coffee_type) and money_slot.make_payment(coffee_type.cost):
                maker.make_coffee(coffee_type)
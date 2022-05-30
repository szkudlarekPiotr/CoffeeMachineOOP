from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

to_continue = True

while to_continue:
    order = input(f"Which coffee would you like? ({menu.get_items()}) ")
    if order.lower() != "off" and order.lower() != "report":
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    elif order.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        to_continue = False

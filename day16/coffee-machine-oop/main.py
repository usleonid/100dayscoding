from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
payment = MoneyMachine()

while True:
    order = input(f"What would you like? ({menu.get_items()}): ").lower()
    if order == "report":
        coffee_maker.report()
        payment.report()
    elif order == "off":
        break
    else:
        if menu.find_drink(order) == None:
            continue
        else:
            beverage = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(beverage) == False:
            continue
        if payment.make_payment(beverage.cost) == False:
            continue
        coffee_maker.make_coffee(beverage)



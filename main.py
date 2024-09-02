from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    coffee_machine_on = True
    my_coffee_maker = CoffeeMaker()
    my_money_machine = MoneyMachine()
    drinks_menu = Menu()

    while coffee_machine_on:
        order_is_valid = False
        print(drinks_menu.get_items())
        choice = input("What would you like? (espresso/latte/cappuccino/):").lower()
        if choice == "off":
            print("Machine was turned OFF")
            coffee_machine_on = False
            continue
        if choice == "report":
            my_coffee_maker.report()
            my_money_machine.report()
            continue

        drink = drinks_menu.find_drink(choice)
        if drink:
            order_is_valid = my_coffee_maker.is_resource_sufficient(drink)
        else:
            print("Wrong choice")
            continue

        if order_is_valid:
            #payment = my_money_machine.process_coins()
            #print(f"{payment}$ was received ")
            order_is_valid = my_money_machine.make_payment(drink.cost)
            if order_is_valid:
                my_coffee_maker.make_coffee(drink)
        else:
            print("Not enough resources. you may choose again")


if __name__ == "__main__":
    main()
    


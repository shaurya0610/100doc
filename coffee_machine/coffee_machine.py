import coffee_machine_data

money_in_machine = 0
current_resources = resources


def coffee_machine():
    global money_in_machine
    global current_resources

    user_input = input("What would you like? (espresso/latte/cappuccino):")

    if user_input == "off":
        return()

    if user_input == "report":
        print(f"Water: {current_resources['water']}")
        print(f"Milk: {current_resources['milk']}")
        print(f"Coffee: {current_resources['coffee']}")
        print(f"Money: {money_in_machine}")
        coffee_machine()

    if user_input == "espresso":
        if current_resources["water"] < 50:
            print("Sorry, there is not enough water.")
            coffee_machine()
        if current_resources["coffee"] < 18:
            print("Sorry, there is not enough coffee.")
            coffee_machine()
    elif user_input == "latte":
        if current_resources["water"] < 200:
            print("Sorry, there is not enough water.")
            coffee_machine()
        if current_resources["milk"] < 150:
            print("Sorry, there is not enough milk.")
            coffee_machine()
        if current_resources["coffee"] < 24:
            print("Sorry, there is not enough coffee.")
            coffee_machine()
    elif user_input == "cappuccino":
        if current_resources["water"] < 250:
            print("Sorry, there is not enough water.")
            coffee_machine()
        if current_resources["milk"] < 100:
            print("Sorry, there is not enough milk.")
            coffee_machine()
        if current_resources["coffee"] < 24:
            print("Sorry, there is not enough coffee.")
            coffee_machine()

    print("Please insert coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))

    money_inserted = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    if user_input == "espresso":
        if money_inserted < 1.5:
            print("Sorry that's not enough money. Money refunded.")
            coffee_machine()
        else:
            print(f"Here is your ${round(money_inserted - 1.5, 2)} in change.")
            money_in_machine += 1.5
    elif user_input == "latte":
        if money_inserted < 2.5:
            print("Sorry that's not enough money. Money refunded.")
            coffee_machine()
        else:
            print(f"Here is your ${round(money_inserted - 2.5, 2)} in change.")
            money_in_machine += 2.5
    elif user_input == "cappuccino":
        if money_inserted < 3.0:
            print("Sorry that's not enough money. Money refunded.")
            coffee_machine()
        else:
            print(f"Here is your ${round(money_inserted - 3.0, 2)} in change.")
            money_in_machine += 3.0

    # TODO 7. Make Coffee.
    # a. If the transaction is successful and there are enough resources to make the drink the
    # user selected, then the ingredients to make the drink should be deducted from the
    # coffee machine resources.
    # E.g. report before purchasing latte:
    # Water: 300ml
    # Milk: 200ml
    # Coffee: 100g
    # Money: $0
    # Report after purchasing latte:
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5
    # b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
    # latte was their choice of drink.

    if user_input == "espresso":
        current_resources["water"] -= 50
        current_resources["coffee"] -= 18
    elif user_input == "latte":
        current_resources["water"] -= 200
        current_resources["milk"] -= 150
        current_resources["coffee"] -= 24
    elif user_input == "cappuccino":
        current_resources["water"] -= 250
        current_resources["milk"] -= 100
        current_resources["coffee"] -= 24

    print(f"Here is your {user_input}. Enjoy!")
    coffee_machine()


coffee_machine()

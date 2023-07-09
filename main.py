from Resources import MENU, resources


# TODO: Check if the resources are sufficient for making the drink
def is_resource_sufficient(drink):
    for item in drink:
        if drink[item] > resources[item]:
            print(f"There is not enough {item}")
            return False
    return True


# TODO: Calculate the change or if the money is not sufficient
def change_calculator():
    # TODO: Get the different no of coins they want to insert
    print("Please insert coins\n")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    total_amt = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    # print(total_amt)
    # print(MENU[drink_type]["cost"])
    if total_amt < MENU[drink_type]["cost"]:
        print("Insufficient funds!")
        return False
    elif total_amt > MENU[drink_type]["cost"]:
        change_amt = total_amt - MENU[drink_type]["cost"]
        print(f"Transaction is successful!Here is your change ${round(change_amt,2)}")
        return True
    else:
        print("Transaction is successful!")
        return True


# TODO: MAke the drink
def make_your_drink(drink):
    if is_resource_sufficient(MENU[drink_type]["ingredients"]) and change_calculator():
        for item in drink:
            resources[item] -= drink[item]
        give_the_drink()


# TODO: give the user their drink
def give_the_drink():
    print(f"Here is your {drink_type}☕ Enjoy!")


# TODO: put an infinite while loop
# TODO: Get the type of drink from the user
while True:
    drink_type = input("""Please type the kind of beverage that you want. You can type 'stop' to stop ordering.\n
What would you like? (espresso/latte/cappuccino): """)

    # TODO: display the current resources balance when the user types "report"
    if drink_type == "report":
        print(resources)
    elif drink_type == "stop":
        break
    else:
        make_your_drink(MENU[drink_type]["ingredients"])

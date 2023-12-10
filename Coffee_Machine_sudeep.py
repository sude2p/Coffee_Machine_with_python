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
    "cost": 0,
}


def report():

    for i in resources:
        print(f"{i} : {resources[i]}")


is_on = True
resource_calc = True


def resource_calculation(user_choice):

    if user_choice == "espresso":
        resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        resources["milk"] = resources["milk"]
        resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        resources["cost"] = profit

    elif user_choice == "latte":
        resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        resources["cost"] = profit
    elif user_choice == "cappuccino":
        resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
        resources["cost"] = profit


def user_payment_info():

    quarters = float(input("How many quarters?: "))*0.25
    dimes = float(input("How many dimes?: "))* 0.1
    nickles = float(input("How many nickles?: "))*0.05
    pennies = float(input("How many pennies?: "))*0.01
    return quarters, dimes, nickles, pennies


def user_payment(user_choice):
    if user_choice == "menu":
        report()

    if user_choice == "espresso":
        if resources["water"] < 50:
            print("Sorry theres no enough water")
            return
        elif resources["coffee"] <= 0:
            print("Sorry theres no enough coffee")
            return
        else:
            quarters, dimes, nickels, pennies = user_payment_info()
            total_payment_espresso = quarters + dimes + nickels + pennies
            price_espresso = MENU[user_choice]["cost"]
            change = total_payment_espresso - price_espresso
            if price_espresso < total_payment_espresso:
                global profit
                profit += price_espresso
                resource_calculation(user_choice)
                print(f"Here is your change $ {change} in change")
                print(f"Here is your {user_choice} Enjoy")

            else:
                print(f"Sorry that's not enough money. ${total_payment_espresso} refunded")

    elif user_choice == "latte":
        if resources["water"] < 200:
            print("Sorry theres no enough water")
            return
        elif resources["milk"] < 150:
            print("Sorry theres no enough milk")
            return
        elif resources["coffee"] < 24:
            print("Sorry theres no enough coffee")
            return

        else:

            quarters, dimes, nickels, pennies = user_payment_info()
            total_payment_latte = quarters + dimes + nickels + pennies
            price_latte = MENU[user_choice]["cost"]
            change = total_payment_latte - price_latte
            if price_latte <= total_payment_latte:
                global profit
                profit += price_latte
                resource_calculation(user_choice)
                print(f"Here is your change $ {change} in change")
                print(f"Here is your {user_choice} Enjoy")

            else:
                print(f"Sorry that's not enough money. ${total_payment_latte} refunded")

    elif user_choice == "cappuccino":
        if resources["water"] < 250:
            print("Sorry theres no enough water")
            return
        elif resources["milk"] < 100:
            print("Sorry theres no enough milk")
            return
        elif resources["coffee"] < 25:
            print("Sorry theres no enough coffee")
            return
        else:
            quarters, dimes, nickels, pennies = user_payment_info()
            total_payment_cappuccino = quarters + dimes + nickels + pennies
            price_cappuccino = MENU[user_choice]["cost"]
            change = total_payment_cappuccino - price_cappuccino
            if price_cappuccino < total_payment_cappuccino:
                global profit
                profit += price_cappuccino
                resource_calculation(user_choice)
                print(f"Here is your change $ {change} in change")
                print(f"Here is your {user_choice} Enjoy")

            else:
                print(f"Sorry that's not enough money. ${total_payment_cappuccino} refunded")


while is_on:
    user_input = input("What would you like? (espresso / latte /cappuccino /menu: ").lower()
    user_payment(user_input)

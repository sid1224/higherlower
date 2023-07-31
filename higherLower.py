# TODO: 1: Take input from user
# TODO 2: Print report on resources remaining
# TODO 3: Ask for coins to be inserted
# TODO 4: Calculate value of inserted coins and give change
# TODO 5: Ask for user input again and check if resources remaining
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


resources_remaining = resources


def calculate_change(quarters, dimes, nickels, pennies, user_choice):
    total_value = ((quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01))
    change = total_value - MENU[user_choice]['cost']
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is ${change} in change")


def resources_left(resources_remaining, user_choice):
    if user_choice == 'latte' or user_choice == 'cappuccino':
        if resources_remaining['water'] < MENU[user_choice]['ingredients']['water']:
            print("Sorry there is not enough water")
        elif resources_remaining['milk'] < MENU[user_choice]['ingredients']['milk']:
            print("Sorry there is not enough milk")
        elif resources_remaining['coffee'] < MENU[user_choice]['ingredients']['coffee']:
            print("Sorry there is not enough coffee")
    elif user_choice == 'espresso':
        if resources_remaining['water'] < MENU[user_choice]['ingredients']['water']:
            print("Sorry there is not enough water")
        elif resources_remaining['coffee'] < MENU[user_choice]['ingredients']['coffee']:
            print("Sorry there is not enough coffee")
    else:
        machine_continue = True
        return machine_continue


def reduce_resources(resources_remaining, user_choice):
    if user_choice == 'latte':
        resources_remaining['water'] = resources_remaining['water']-MENU[user_choice]['ingredients']['water']
        resources_remaining['milk'] = resources_remaining['milk'] - MENU[user_choice]['ingredients']['milk']
        resources_remaining['coffee'] = resources_remaining['coffee'] - MENU[user_choice]['ingredients']['coffee']
    elif user_choice == 'espresso':
        resources_remaining['water'] = resources_remaining['water'] - MENU[user_choice]['ingredients']['water']
        resources_remaining['coffee'] = resources_remaining['coffee'] - MENU[user_choice]['ingredients']['coffee']
    elif user_choice == 'cappuccino':
        resources_remaining['water'] = resources_remaining['water'] - MENU[user_choice]['ingredients']['water']
        resources_remaining['milk'] = resources_remaining['milk'] - MENU[user_choice]['ingredients']['milk']
        resources_remaining['coffee'] = resources_remaining['coffee'] - MENU[user_choice]['ingredients']['coffee']


use_machine = True
while use_machine:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'report':
        print(resources_remaining)
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    elif user_choice == 'latte' or user_choice == 'espresso' or user_choice == 'cappuccino':
        make_coffee = resources_left(resources_remaining, user_choice)
        if make_coffee:
            print("Please insert coins")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            calculate_change(quarters, dimes, nickels, pennies, user_choice)
            print(f"Here is your {user_choice}!☕️")
            reduce_resources(resources_remaining, user_choice)
    elif user_choice == 'off':
        use_machine = False



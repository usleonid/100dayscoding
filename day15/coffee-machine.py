from base_information import MENU, resources


while True:
    user_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_prompt == 'espresso' or user_prompt == 'latte' or user_prompt == 'cappuccino':
        for ingredient in MENU[user_prompt]['ingredients']:
            if MENU[user_prompt]['ingredients'][ingredient] > resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                break
            # resources[ingredient] -= MENU[user_prompt]['ingredients'][ingredient]
            # resources[money] += MENU[user_prompt]['cost']
    elif user_prompt == 'report':
        for resource in resources:
            if resource == 'water' or resource == 'milk':
                unit = 'ml'
            elif resource == 'coffee':
                unit = 'g'
            elif resource == 'money':
                unit = '$'
            if resource != 'money':
                print(f"{resource}: {resources[resource]}{unit}")
            else:
                print(f"{resource}: {unit}{resources[resource]}")
        continue
    elif user_prompt == 'off':
        break
    else:
        print('Unknown command. Please retype!')
        continue

    print("Please insert coins.")

    quarters = 0.25 * int(input("how many quarters?: "))
    dimes = 0.1 * int(input("how many dimes?: "))
    nickles = 0.05 * int(input("how many nickles?: "))
    pennies = 0.01 * int(input("how many pennies?: "))

    payment = quarters + dimes + nickles + pennies

    if payment >= MENU[user_prompt]['cost']:
        if payment > MENU[user_prompt]['cost']:
            change = payment - MENU[user_prompt]['cost']
            print(f"Here is ${round(change,2)} in change.")
        print(f"Here is your {user_prompt} ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")
        continue

    for ingredient in MENU[user_prompt]['ingredients']:
        resources[ingredient] -= MENU[user_prompt]['ingredients'][ingredient]
    resources['money'] += MENU[user_prompt]['cost']





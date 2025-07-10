from art import logo
from menu import MENU, resources

"""
1. print report
    print how much of each resource there is including money
2. check if sufficient resources
    if not enough of either resource, give user feedback of deficient resource
    loop back to ask what the user wants
3. process coins
    ask user to insert coins
    ask how many coins of each value: quarter, dime, nickle, penny (input)
    calculate total of coins
        if enough or more money, "dispense" coffeee and/or calculate amount to refund
    loop back to ask what the user wants
4. check transaction successful
    if not enough coins, let user know it is not enough and "refund" their money
5. make coffee
    deduct resources per coffee that was made
end execution of the code with an "off" keyword - to exit the while loop
"""

def is_resource_sufficient(order_ingredients):
    """Returns True if order can be made or False when insufficient resources"""
    is_enough = True
    
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    
    return is_enough

def process_coins():
    """Returns total calculated from inserted coins"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * .25
    total += int(input("How many dimes?: ")) * .10
    total += int(input("How many nickles?: ")) * .05
    total += int(input("How many pennies?: ")) * .01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when payment accepted or False when insufficient money"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"“Here is ${change} dollars in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from resources"""
    for item in order_ingredients:
        #sub the required ingredients from the resources
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")
    
print(logo)
profit = 0
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappucino)").lower()
    
    #keyword to "shut down" the coffee machine
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

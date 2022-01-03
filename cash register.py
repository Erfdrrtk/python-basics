# source: Python - Code along - Simple "Cashier Program"
# link: https://www.youtube.com/watch?v=gFURWvmUbSU
# inventory containing items and prices
inventory = {'grapes': 10, 'pizza': 50, 'eggs': 30, 'tomato': 25}

basket = []
total = []
def cashier():
    print(f"this is our inventory: {inventory}")
    user_answer = input("what would you like to purchase? ").lower()
    while user_answer != "quit":
        if user_answer in inventory:
            basket.append(user_answer)
            user_answer = input('anything else? (type quit to end) ').lower()
        else:
            user_answer = input('''that is not in our inventory.:(type quit to end or add an item to your basket) ''')

cashier()
print(f"here are all the items in your shopping cart {basket}")

answer = input("anything else. (yes or no) ")

if answer == 'yes':
    cashier()
    print(f"here is your items {basket}")
    for items in basket:
        total.append(inventory[items])
    amount_to_pay = sum(total)
else:
    for items in basket:
        total.append(inventory[items])
    amount_to_pay = sum(total)
print(f"your total amount is: ${amount_to_pay}")

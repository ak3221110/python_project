menu = {
    'pizza': 50,
    'Pizza': 50,
    'coffee': 60,
    'Coffee': 60,
    'tea': 10,
    'Tea': 10,
    'drink': 20,
    'Drink': 20,
}

total_price = 0

# Greet the user
print("Welcome to our restaurant, here is our menu:")
print('''
Pizza: 50
Coffee: 60
Tea: 10
Drink: 20
''')

while True:
    item = input("Enter an item you want (or type 'done' to finish): ")
    
    if item.lower() == 'done':
        break
    
    if item in menu:
        total_price += menu[item]
        print(f"Your item '{item}' is added.")
    else:
        print("Sorry, please tell me another item.")

    # Ask if they want to add another item
    another_item = input("Do you want to add another item? (yes/no): ").strip().lower()
    if another_item == 'no':
        print("Thank you for your order!")
        break
    elif another_item != 'yes':
        print("Invalid response. Please answer with 'yes' or 'no'.")

# Final output
print("Your total amount is:", total_price)

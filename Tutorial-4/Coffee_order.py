print("Welcome to the Python Coffee Shop!")

customer_name = input("What is your name? ")
print("Hello, " + customer_name + "! Let's order some coffee.")

# Drink menu with prices
menu = {
    "coffee": 3.50,
    "latte": 4.00,
    "mocha": 4.50,
    "cappuccino": 4.20
}

# Show menu
print("\nMenu:")
for drink, price in menu.items():
    print(f"{drink.capitalize()}: ${price}")

# Check if customer is a student
student = input("\nAre you a student? (yes/no): ").lower()
student_discount = 0.10 if student == "yes" else 0

# Grand total for all orders
grand_total = 0

# Loop to take multiple orders
while True:
    order_input = input("\nEnter your order (e.g., '1 coffee, 3 latte'): ").lower()
    
    # Split the order into items
    order_items = order_input.split(",")
    
    total_cost = 0  # total for this round
    
    for item in order_items:
        item = item.strip()  # remove extra spaces
        if not item:
            continue
        
        try:
            quantity_str, drink = item.split(" ", 1)
            quantity = int(quantity_str)
        except ValueError:
            print(f"Invalid format for item: {item}")
            continue
        
        if drink in menu:
            cost = menu[drink] * quantity
            
            # Discount for more than 1 cup of the same drink
            if quantity > 1:
                print(f"You get a discount of $1.00 on {drink}!")
                cost -= 1.00
            
            total_cost += cost
        else:
            print(f"Sorry, we do not have {drink}.")
    
    # Apply student discount
    if student_discount > 0 and total_cost > 0:
        discount_amount = total_cost * student_discount
        total_cost -= discount_amount
        print(f"Student discount applied: ${discount_amount:.2f}")
    
    print(f"Total for this order: ${total_cost:.2f}")
    
    # Add to grand total
    grand_total += total_cost
    
    another_order = input("\nWould you like to order another round? (yes/no): ").lower()
    if another_order == "no":
        break

print(f"\nGrand total for all orders: ${grand_total:.2f}")
print(f"Thank you, {customer_name}! Please come again.")

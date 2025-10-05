# list items and prices
items = ["artisan sandwich", "decaf", "earl grey tea", "croissant", "cappucchino"]
prices = [9.99, 4.99, 2.99, 3.99, 4.59]

# display the list of items with prices
print("--WELCOME TO THE BOOKNOOK--")
print("\nItems for sale:")
for i in range(len(items)):
    print(f"{i + 1}. {items[i]} - ${prices[i]}")

# storing selected items and total cost
cart = []
total = 0.0

print("\nType the number of the item you want to buy.")
print("Type 'done' to checkout.\n")

# loop for multiple purchases
while True:
    choice = input("Your choice: ").strip().lower()

    if choice == 'done':
        break

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(items):
            cart.append(items[index])
            total += prices[index]
            print(f"Added {items[index]} to your cart.")
        else:
            print("Invalid number. Please choose a valid item number.")
    else:
        print("Please enter a number or type 'done' to finish.")

# discount
discount_code = "CAPPUCCINO"
discount_percent = 20  # 20%
apply_discount = False

user_code = input("\nDo you have a discount code? Enter it or press Enter to skip: ").strip()

if user_code.upper() == discount_code:
    apply_discount = True
    discount_amount = total * (discount_percent / 100)
    total -= discount_amount
    print(f"Discount code applied! You saved ${discount_amount:.2f}.")

# receipt
print("\n----- Receipt -----")
for item in cart:
    print(f"- {item}")
print(f"Total: ${total:.2f}")
print("-------------------")
print("Thank you for stopping by!")
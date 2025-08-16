''' Create a function named calculate_discount(price, discount_percent) that calculates the final
 price after applying a discount. The function should take the original price (price) and the 
 discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply
the discount; otherwise, return the original price.
'''
def calculate_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Print result
if discount_percent >= 20:
    print(f"Discount applied. The final price is: {final_price:.2f}")
else:
    print(f"No discount applied. The price remains: {final_price:.2f}"
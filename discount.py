def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Applies the discount only if it is 20% or higher.
    
    Args:
    - price (float): Original price of the item.
    - discount_percent (float): Discount percentage to apply.
    
    Returns:
    - float: Final price after applying the discount, or the original price if no discount is applied.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for inputs
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate and display the final price
    final_price = calculate_discount(original_price, discount_percentage)
    if discount_percentage >= 20:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
except ValueError:
    print("Please enter valid numerical values for the price and discount percentage.")

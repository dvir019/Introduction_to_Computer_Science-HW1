def main():
    """
    The program gets the price and the quantity of four products,
    and prints the following information about the purchase:
    - If it's valid: - The total price of the purchase
                     - The total products quantity
                     - The average unit price
    - If it's invalid: A message that the purchase is invalid
    """

    # Set the types of the products
    a_type = "A"
    b_type = "B"
    c_type = "C"
    d_type = "D"

    # Get the price and the quantity of product A
    print(f"{a_type}:")
    a_unit_price = float(input())
    a_quantity = int(input())

    # Get the price and the quantity of product B
    print(f"{b_type}:")
    b_unit_price = float(input())
    b_quantity = int(input())

    # Get the price and the quantity of product C
    print(f"{c_type}:")
    c_unit_price = float(input())
    c_quantity = int(input())

    # Get the price and the quantity of product D
    print(f"{d_type}:")
    d_unit_price = float(input())
    d_quantity = int(input())

    # Check if all of the prices are non-negative
    is_prices_valid = (a_unit_price >= 0) \
                      and (b_unit_price >= 0) \
                      and (c_unit_price >= 0) \
                      and (d_unit_price >= 0)

    # Check if the prices of products A and B are valid
    is_prices_valid = is_prices_valid \
                      and (a_unit_price <= 50) \
                      and (b_unit_price <= 30)

    # Check if all of the quantities are non-negative
    is_quantities_valid = (a_quantity >= 0) \
                          and (b_quantity >= 0) \
                          and (c_quantity >= 0) \
                          and (d_quantity >= 0)

    # Check if the quantities of products A, C and D are valid
    is_quantities_valid = is_quantities_valid \
                          and (d_quantity > 0) \
                          and (a_quantity + c_quantity <= 5)

    # Check if the whole purchase is valid
    is_purchase_valid = is_prices_valid and is_quantities_valid

    # Calculate the total prices
    a_total_price = a_quantity * a_unit_price
    b_total_price = b_quantity * b_unit_price
    c_total_price = c_quantity * c_unit_price
    d_total_price = d_quantity * d_unit_price
    total_price = a_total_price + b_total_price + c_total_price + d_total_price

    # Calculate the total products quantity
    total_quantity = a_quantity + b_quantity + c_quantity + d_quantity

    # Calculate the average unit price
    unit_average_price = total_price / total_quantity

    # Generate the printing message, by multiply the string in zero or one, depends on the value of the boolean
    message_to_print = f"{total_price:.2f} {total_quantity} {unit_average_price:.2f}" * int(is_purchase_valid)
    message_to_print += f"Invalid Purchase" * int(not is_purchase_valid)

    # Print the message
    print(message_to_print)


if __name__ == '__main__':
    main()

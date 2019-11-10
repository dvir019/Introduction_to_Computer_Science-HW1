def main():
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
    is_prices_valid = (a_unit_price >= 0) * (b_unit_price >= 0) * (c_unit_price >= 0) * (d_unit_price >= 0)

    # Check if the prices of products A and B are valid
    is_prices_valid *= (a_unit_price <= 50) * (b_unit_price <= 30)

    # Check if all of the quantities are non-negative
    is_quantities_valid = (a_quantity >= 0) * (b_quantity >= 0) * (c_quantity >= 0) * (d_quantity >= 0)

    # Check if the quantities of products A, C and D are valid
    is_quantities_valid *= (d_quantity > 0) * (a_quantity + c_quantity <= 5)

    # Check if the whole purchase is valid
    is_purchase_valid = is_prices_valid * is_quantities_valid

    # Calculate the total prices
    a_total_price = a_quantity * a_unit_price
    b_total_price = b_quantity * b_unit_price
    c_total_price = c_quantity * c_unit_price
    d_total_price = d_quantity * d_unit_price
    total_price = a_total_price + b_total_price + c_total_price + d_total_price

    # Calculate the total quantities
    total_quantity = a_quantity + b_quantity + c_quantity + d_quantity

    # Calculate the average price of the units
    unit_average_price = total_price / total_quantity

    # Generate the printing message
    message_to_print = f"{total_price:.2f} {total_quantity} {unit_average_price:.2f}" * bool(is_purchase_valid)
    message_to_print += f"Invalid Purchase" * bool(1 - is_purchase_valid)

    # Print the message
    print(message_to_print)


if __name__ == '__main__':
    main()

def main():
    # Set the types
    a_type = "A"
    b_type = "B"
    c_type = "C"
    d_type = "D"

    # TODO - find good documentation
    print(f"{a_type}:\n")
    a_unit_price = int(input())
    a_quantity = int(input())

    # TODO - find good documentation
    print(f"{b_type}:\n")
    b_unit_price = int(input())
    b_quantity = int(input())

    # TODO - find good documentation
    print(f"{c_type}:\n")
    c_unit_price = int(input())
    c_quantity = int(input())

    # TODO - find good documentation
    print(f"{d_type}:\n")
    d_unit_price = int(input())
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


if __name__ == '__main__':
    main()

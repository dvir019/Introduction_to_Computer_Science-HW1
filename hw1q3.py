def main():
    """
    The program gets information about six cards - three for each player,
    and calculates the winner, based on the weight of the cards.
    - First card  - A letter
    - Second card - A three digit number
    - Third card  - A letter
    """

    # Get the cards of player A
    print("Player A,")
    print("Insert 1st card:")
    a_first_card = input()
    print("Insert 2nd card:")
    a_second_card = int(input())
    print("Insert 3rd card:")
    a_third_card = input()

    # Get the cards of player A
    print("Player B,")
    print("Insert 1st card:")
    b_first_card = input()
    print("Insert 2nd card:")
    b_second_card = int(input())
    print("Insert 3rd card:")
    b_third_card = input()

    # Calculate the weight of the first card of player A
    ord_value = ord(a_first_card)
    a_first_card_weight = ord_value - ord('A')  # Assume it's uppercase
    if ord('a') <= ord_value <= ord('z'):  # Check if it's lowercase
        a_first_card_weight = ord_value - ord('a')

    # Calculate the weight of the second card of player A
    units_digit = a_second_card % 10
    a_second_card //= 10
    tens_digit = a_second_card % 10
    a_second_card //= 10
    hundreds_digit = a_second_card % 10
    a_second_card_weight = (tens_digit ** units_digit) // hundreds_digit

    # Calculate the weight of the third card of player A
    ord_value = ord(a_third_card)
    a_third_card_weight = 0  # Assume it's zero
    if ord_value % 7 == 0:
        a_third_card_weight = 17
    elif ord_value % 4 == 0:
        a_third_card_weight = 6

    # Calculate the total cards weight of player A
    a_cards_total_weight = a_first_card_weight + a_second_card_weight + a_third_card_weight

    # Calculate the weight of the first card of player B
    ord_value = ord(b_first_card)
    b_first_card_weight = ord_value - ord('A')  # Assume it's uppercase
    if ord('a') <= ord_value <= ord('z'):  # Check if it's lowercase
        b_first_card_weight = ord_value - ord('a')

    # Calculate the weight of the second card of player B
    units_digit = b_second_card % 10
    b_second_card //= 10
    tens_digit = b_second_card % 10
    b_second_card //= 10
    hundreds_digit = b_second_card % 10
    b_second_card_weight = (tens_digit ** units_digit) // hundreds_digit

    # Calculate the weight of the third card of player B
    ord_value = ord(b_third_card)
    b_third_card_weight = 0  # Assume it's zero
    if ord_value % 7 == 0:
        b_third_card_weight = 17
    elif ord_value % 4 == 0:
        b_third_card_weight = 6

    # Calculate the total cards weight of player B
    b_cards_total_weight = b_first_card_weight + b_second_card_weight + b_third_card_weight

    # Calculate the final result of the game
    game_result = "It's a tie."  # Assume it's a tie
    if a_cards_total_weight > b_cards_total_weight:
        game_result = "The winner is Player A!"
    elif b_cards_total_weight > a_cards_total_weight:
        game_result = "The winner is Player B!"
    elif a_second_card_weight > b_second_card_weight:
        game_result = "The winner is Player A!"
    elif b_second_card_weight > a_second_card_weight:
        game_result = "The winner is Player B!"

    # Print the results
    print(f"Score A - total:{a_cards_total_weight}, card2:{a_second_card_weight}")
    print(f"Score B - total:{b_cards_total_weight}, card2:{b_second_card_weight}")
    print(game_result)


if __name__ == '__main__':
    main()

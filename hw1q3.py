def main():
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
    a_first_card_weight = ord('A') - ord(a_first_card)
    if ord('a') <= ord(a_first_card) <= ord('z'):
        a_first_card_weight = ord('a') - ord(a_first_card)

    # Calculate the weight of the second card of player A
    units_digit = a_second_card % 10
    a_second_card //= 10
    tens_digit = a_second_card % 10
    a_second_card //= 10
    hundreds_digit = a_second_card % 10
    a_second_card_weight = (tens_digit ** units_digit) // hundreds_digit

    # Calculate the weight of the third card of player A
    a_third_card_weight = 0
    if a_third_card % 7 == 0:
        a_third_card_weight = 17
    elif a_third_card % 4 == 0:
        a_third_card_weight = 6

    # Calculate the total cards weight of player A
    a_cards_total_weight = a_first_card_weight + a_second_card_weight + a_third_card_weight











    # Calculate the weight of the first card of player B
    b_first_card_weight = ord('A') - ord(b_first_card)
    if ord('a') <= ord(b_first_card) <= ord('z'):
        b_first_card_weight = ord('a') - ord(b_first_card)

    # Calculate the weight of the second card of player B
    units_digit = b_second_card % 10
    b_second_card //= 10
    tens_digit = b_second_card % 10
    b_second_card //= 10
    hundreds_digit = b_second_card % 10
    b_second_card_weight = (tens_digit ** units_digit) // hundreds_digit

    # Calculate the weight of the third card of player B
    b_third_card_weight = 0
    if b_third_card % 7 == 0:
        b_third_card_weight = 17
    elif b_third_card % 4 == 0:
        b_third_card_weight = 6

    # Calculate the total cards weight of player B
    b_cards_total_weight = b_first_card_weight + b_second_card_weight + b_third_card_weight

    # Calculate the final result of the game



if __name__ == '__main__':
    main()

"""
Написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей. 
Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.
"""

import random

def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list[int]:
    """
    A function that creates and returns a sorted list of random unique elements from min_value to max_value by quantity of elements. 
    Args:
        * min_value (int): minimum value of the range
        * max_value (int): maximum value of the range
        * quantity (int): quantity of elements in the list
    Returns:
        * list[int]: sorted list of random unique elements from min_value to max_value by quantity of elements
    """
    try:
        if not 1 <= min_value < max_value <= 1000:
            raise ValueError("Min should be > 1, Max should be < 1000, Max should be greater than Min.")
        if quantity > (max_value - min_value + 1):
            raise ValueError("Quantity should be in the range between Min and Max.")

        set_values = random.sample(range(min_value, max_value + 1), quantity)
    except ValueError as e:
        print(f"Error while generating numbers: {e}")
        return []

    set_values.sort()
    return set_values

def get_valid_input_number(message: str) -> int:
    """
    A function that prompts for user input until an integer value is entered.
    Args: 
        * message (str): the message to display to the user.
    Returns:
        * number (int): entered integer value
    """
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError as e:
            print(f"{e},  value must be of type integer")


min_user_value= get_valid_input_number("Enter a number for the MIN value >>>> ")
max_user_value = get_valid_input_number("Enter a number for the MAX value >>>> ")
quantity_user_value = get_valid_input_number("Enter a number for the QUANTITY value >>>> ")

result = get_numbers_ticket(min_user_value, max_user_value, quantity_user_value)
print(result)

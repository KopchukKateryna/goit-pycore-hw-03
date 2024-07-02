"""
Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату,
залишаючи тільки цифри та символ '+' на початку. Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі
та перетворює його на стандартний формат, залишаючи тільки цифри та символ '+'. 
Якщо номер не містить міжнародного коду, функція автоматично додає код '+38' (для України). 
Це гарантує, що всі номери будуть придатними для відправлення SMS.
"""
import re

def normalize_phone(phone_number: str) -> str:
    """
    A function that takes a phone number, removes all characters from it except digits and the + sign.
    Returns a normalized number starting with the +38 prefix.
    Args: 
        * phone_number (str): phone number.
    Returns:
        * str: normalized phone number with the +38 prefix.
    """
    cleaned_phone_number = re.sub(r'[^0-9+]', '', phone_number)
    if cleaned_phone_number.startswith('0'):
        cleaned_phone_number = f"+38{cleaned_phone_number}"
    elif cleaned_phone_number.startswith('38'):
        cleaned_phone_number = f"+{cleaned_phone_number}"
    return cleaned_phone_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# !
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS mass messaging\n", sanitized_numbers)

# ! the same func call is:
# sanitized_numbers = []
# for num in raw_numbers:
#     sanitized_numbers.append(normalize_phone(num))
# print(sanitized_numbers)

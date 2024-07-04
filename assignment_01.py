'''
Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

Критерії оцінювання:

Коректність роботи функції: функція повинна точно обраховувати кількість днів між датами.
Обробка винятків: функція має впоратися з неправильним форматом вхідних даних.
Читабельність коду: код повинен бути чистим і добре документованим.
'''

from datetime import datetime
import re

def get_days_from_today(date: str) -> int:
    """
    The function that calculates the number of days between a given date and the current date.
    Args:
        * date (str): a date in ISO format ('YYYY-MM-DD')
    Returns:
        * days_difference (int): the difference in days as an integer. 
    """
    
    while True:
        try:
            match = re.match(r"^(\d{4}-\d{2}-\d{2}).*", date)
            if not match:
                raise ValueError("Date must start with 'YYYY-MM-DD' format, but got: {date}")
            date_given = datetime.strptime(match.group(1), '%Y-%m-%d').date()
            break
        except ValueError as e:
            date = input(f"{e}. Please, enter a date in ISO format => 'YYYY-MM-DD' >>>> ")

    date_today = datetime.today().date()
    days_difference = (date_today - date_given).days
    day_word_sing_plur = 'day' if days_difference == 1 or days_difference == -1 else 'days'
    print(f"The difference between {date_given} and today {date_today} is {days_difference} {day_word_sing_plur}.")

    return days_difference

user_date = input("Please, enter a date in ISO format => 'YYYY-MM-DD' >>>> ")
get_days_from_today(user_date)

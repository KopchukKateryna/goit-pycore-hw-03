"""
Створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати.
Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.
"""
from datetime import datetime, timedelta

users_list = [
    {'name': 'Diana Johnson', 'birthday': '1966.11.09'},
    {'name': 'Kevin Moore', 'birthday': '1996.07.03'},
    {'name': 'Laura Taylor', 'birthday': '1967.07.05'},
    {'name': 'Jane Williams', 'birthday': '2010.07.08'},
    {'name': 'Kevin Jackson', 'birthday': '1976.07.06'},
    {'name': 'Edward Garcia', 'birthday': '1967.07.02'},
    {'name': 'Diana Jackson', 'birthday': '2020.07.11'},
    {'name': 'Laura Williams', 'birthday': '1963.07.13'},
    {'name': 'Michael Anderson', 'birthday': '1977.08.18'},
    {'name': 'George Miller', 'birthday': '1996.03.24'}
    ]

def get_upcoming_birthdays(users: dict) -> dict:
    """
    A function that identifies users with birthdays in the next 7 days, including today, and adjusts the congratulation 
    date if the birthday falls on a weekend.
    Args: 
        * users (dict): A dictionary of users with their names and birthdays.
    Returns: 
     * dict: A dictionary of users with their names and birthdays, with the congratulation date adjusted if
    """
    birthdays = []
    date_today = datetime.today().date()
    date_today_plus_week = date_today + timedelta(days=7)
    for user in users:
        try:
            user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except ValueError:
            print(f"The user {user['name']} has incorrect format of birthday.")
        user_birthday = user_birthday.replace(year=date_today.year)
        if date_today <= user_birthday <= date_today_plus_week:
            if user_birthday.weekday() in [5,6]:
                user_birthday += timedelta(days=(7 - user_birthday.weekday()))
            
            birthdays.append({
                'name': user["name"],
                'congratulation_date': user_birthday.strftime('%Y.%m.%d')
            })

    return birthdays

upcoming_birthdays = get_upcoming_birthdays(users_list)
print("List of upcoming birthdays in the current week: ", upcoming_birthdays)

from application import salary, people
from datetime import date

def date_today():
    today = date.today()
    print(today)


if __name__ == '__main__':
    salary.calculate_salary(8987)
    people.get_employees('Georg')
    date_today()


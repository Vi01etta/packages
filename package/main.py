from datetime import datetime

today_time = datetime.today()

print("Текущая дата: ", today_time)

from application import salary

from application.db import people

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
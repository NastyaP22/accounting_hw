from datetime import datetime

from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    calculate_salary(3000, 16)
    get_employees('Антон Петров')
    print(datetime.now())
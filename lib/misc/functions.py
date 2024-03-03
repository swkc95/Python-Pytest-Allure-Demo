from datetime import datetime


def first_day_of_next_month():
    current_date = datetime.now()

    next_month_year = current_date.year
    next_month = current_date.month + 1
    if next_month > 12:
        next_month = 1
        next_month_year += 1

    return datetime(next_month_year, next_month, 1)

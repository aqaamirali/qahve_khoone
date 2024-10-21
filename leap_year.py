print("This program will show you the leap years\n")


def is_leap(year):
    """checks whether year is leap or not"""
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = month_days[month - 1]
    if is_leap(year) and month == 2:
        return f"{year} Is A Leap_Year! and {month} have 29 days! "
    elif is_leap(year):
        return f"{year} Is A Leap_Year! and {month} have {day} days! "
    else:
        return f"{year} Is Not a Leap_Year!"


Year = int(input("Hi, Please Enter a Year:"))
month = int(input("Please Enter a Number of a Month:"))
days = days_in_month(Year, month)
print(days)

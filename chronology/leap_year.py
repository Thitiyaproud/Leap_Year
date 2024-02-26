"""Leap Year utility."""

# Standard Library

# 3rd Party Library

# Project Library

#----------------------------------------------------------------------------------------------------------

def is_leap_year(year: int):
    """Determine if leap is a leap year."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
"""
datetime constructor: datetime(year, month, day, hour, minute, second)
------------------------------------------------
date constructor: datetime.date(year, month, day)
------------------------------------------------
converting to and from date strings
------------------------------------------------
 datetime.strftime -> instance method to convert a datetime to a string
 datetime.strptime -> class method to parse a datetime from a string
------------------------------------------------

the locale's...
    1. weekday name              -> abb (%a) or full (%A)
    2. weekday as decimal number -> %w (0 == sunday...6 == saturday)
    3. day of month              -> %d
    4. month name                -> abb (%b) or full (%B)
    5. month as number           -> %m
    6. year                      -> abb (%y) or full (%Y)
    7. hour                      -> %H
    8. hour (12-hour clock)      -> %I
    9. AM/PM                     -> %p
    8. minute                    -> %M
    9. second                    -> %S
    10. microsecond              -> %f
    11. utc offset               -> %z
    12. timezone name            -> %Z
    13. day of year              -> %j
    14. week of year (sunday)    -> %U
    15. week of year (monday)    -> %W
"""

from datetime import datetime, timedelta
from datetime import date
from typing import Union
from pprint import PrettyPrinter


def get_current_date_and_time():
    now = datetime.now()
    date_only = now.date()
    time_only = now.time()
    return [date_only, time_only]


def get_specific_date():
    """datetime(year, month, day, hour, minute, second)"""
    return datetime(1776, 7, 4, 14, 30, 30)


def get_day_of_week(date_string: str) -> str:
    date_instance = datetime.strptime(date_string, "%m/%d/%Y %H:%M:%S")
    return date_instance.strftime("%A %d %b %Y, %I:%M%p")


def running_and_sleeping_until_new_year():
    new_years_day = datetime(2025, 1, 1, 1, 1, 5)
    curr_date = datetime.today()
    delta_instance = new_years_day - curr_date

    hours_per_day = timedelta(days=1) / timedelta(hours=1)  # Hours in a day
    sleep = timedelta(hours=8)  # Sleep hours in a day
    running = timedelta(minutes=25)
    morning_work_session = timedelta(hours=2.5)

    available_runs_left_2024 = delta_instance.days / 2
    laps_left_in_2024 = available_runs_left_2024 * 6  # assuming 6 laps per run
    running_in_seconds_2024 = running.total_seconds() * available_runs_left_2024
    running_in_days_2024 = (
        running.total_seconds() * available_runs_left_2024
    ) / timedelta(days=1).total_seconds()
    running_in_min_2024 = (
        running.total_seconds() * available_runs_left_2024
    ) / timedelta(minutes=1).total_seconds()
    available_nights_left_2024 = delta_instance.days
    sleeping_in_seconds_2024 = sleep.total_seconds() * delta_instance.days
    sleeping_in_days_2024 = (sleep.total_seconds() * delta_instance.days) / timedelta(
        days=1
    ).total_seconds()
    sleeping_in_min_2024 = (sleep.total_seconds() * delta_instance.days) / timedelta(
        minutes=1
    ).total_seconds()
    return {
        "runs_left_in_2024": available_runs_left_2024,
        "runs_left_in_days": running_in_days_2024,
        "runs_left_in_seconds": running_in_seconds_2024,
        "runs_left_in_minutes": running_in_min_2024,
        "laps_left_in_2024": laps_left_in_2024,
        "nights_left_in_2024": available_nights_left_2024,
        "sleep_left_in_days": sleeping_in_days_2024,
        "sleep_left_in_seconds": sleeping_in_seconds_2024,
        "sleep_left_in_minutes": sleeping_in_min_2024,
    }


def days_past():
    first_day_2024 = datetime(2024, 1, 1, 1, 1, 5)
    curr_date = datetime.today()
    delta = curr_date - first_day_2024
    return delta.days


def greet_person(first_name, last_name, age):
    print(f"Hello, {first_name} {last_name}! You are {age} years old.")


def how_many_sessions():
    pass


def get_requested_date(
    datetime_instance: Union[datetime, date, str]
) -> Union[datetime, date, str]:
    if isinstance(datetime_instance, datetime):
        # return string mm-dd-YYYY HH:MM:SS
        return datetime_instance.strftime("%m-%d-%Y %H:%M:%S")
    elif isinstance(datetime_instance, date):
        # return string mm-dd-YYYY
        return datetime_instance.strftime("%m-%d-%Y")
    elif isinstance(datetime_instance, str):
        try:
            # parse datetime
            datetime.strptime(datetime_instance, "%m/%d/%y %H:%M:%S")
        except Exception:
            # parse date only
            datetime.strptime(datetime_instance, "%m/%d/%y")
    else:
        raise ValueError("problem with given date variable")


if __name__ == "__main__":
    pp = PrettyPrinter(indent=4)
    """
    pp.pprint("get the current date and time:")
    curr_date, curr_time = get_current_date_and_time()
    pp.pprint(f"{curr_date} {curr_time}")
    pp.pprint("get 07/04 1776 at 2:30pm")
    pp.pprint(get_specific_date())
    pp.pprint("get the requested datetime object as a string")
    nov = datetime(2024, 11, 7, 13, 33, 34)

    other_date = date(2024, 4, 14)
    pp.pprint(get_requested_date(other_date))
    """
    pp.pprint("get days until new years 2025")
    pp.pprint(running_and_sleeping_until_new_year())

    # person_info = {"first_name": "John", "last_name": "Doe", "age": 30}

    # greet_person(**person_info)

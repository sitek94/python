"""
Time CalculatorPassed

https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator
"""


def add_time(start_time, duration, start_day=None):
    start_time, am_or_pm = start_time.split()
    start_time_minutes = get_minutes(start_time)

    if am_or_pm == 'PM':
        start_time_minutes += 12 * 60

    duration_minutes = get_minutes(duration)
    total_minutes = start_time_minutes + duration_minutes

    # Calc hours and minutes
    hours = int(total_minutes / 60) % 24
    minutes = total_minutes % 60

    # Append AM/PM suffix
    suffix = 'AM'
    if hours >= 12:
        suffix = 'PM'
        hours -= 12

    # 00:03 => 12:03
    if hours == 0:
        hours = 12

    # 12:3 => 12:03
    if len(str(minutes)) == 1:
        minutes = '0' + str(minutes)

    # E.g. 12:03 PM
    output = str(hours) + ':' + str(minutes) + ' ' + suffix

    # How many days have passed?
    full_days = int(total_minutes / 60 / 24)

    # If we have a start day, add it to the output
    if start_day:
        weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day_index = weekdays.index(start_day.lower()) + 1
        weekday = (day_index + full_days) % 7 - 1

        output += ', ' + weekdays[weekday].capitalize()

    # Append text if result is at least the next day
    if full_days == 1:
        output += ' (next day)'
    if full_days > 1:
        output += ' (' + str(full_days) + ' days later)'

    print(output)
    return output


# Helper to extract minutes
def get_minutes(time):
    hours, minutes = time.split(':')
    hours = int(hours)
    minutes = int(minutes)
    return hours * 60 + minutes


add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)

add_time("8:16 PM", "466:02")
# Returns: 6:18 AM (20 days later)

add_time("8:16 PM", "466:02", "tuesday")
# Returns: 6:18 AM, Monday (20 days later)

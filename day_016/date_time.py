from datetime import datetime

now = datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
current_timestamp = datetime.timestamp(now)

print(f"Current Date: {current_month}/{current_day}/{current_year}")
print(f"Current Time: {current_hour}:{current_minute}")
print(f"Timestamp: {current_timestamp}")


formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Formatted Date: {formatted_date}")


time_string = "5 December, 2019"
time = datetime.strptime(time_string, "%d %B, %Y")
print(f"Time: {time}")


new_year = datetime(current_year + 1, 1, 1)
time_diff = new_year - now
print(f"Time until New Year: {time_diff}")


    # Working with dates and times in different formats
    # Performing date and time arithmetic, such as adding or subtracting days, hours, or minutes from a date or time
    # Comparing dates and times to determine which is earlier or later
    # Formatting dates and times for display in a variety of formats
    # Parsing dates and times from strings in various formats
    # Converting between time zones
    # Working with time intervals, such as calculating the duration between two dates or times.
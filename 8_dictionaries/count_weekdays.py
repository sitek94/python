file_name = 'random_dates.csv'
file_handle = open(file_name)

weekdays = {}

for line in file_handle:
    # E.g. line: "Sunday, 30 May 2021"
    weekday = line.split('"')[1].split(",")[0]
    weekdays[weekday] = weekdays.get(weekday, 0) + 1

for key in weekdays:
    print(key + ':', weekdays[key])

"""SPINTEK kodutöö Karl Erik Seeder 29.03.2022"""

import csv
import datetime
import sys

import holidays

if len(sys.argv) > 1:
    year = int(sys.argv[1])
else:
    print("Error, parameter year not defined")
    exit(1)
holidays = holidays.EE(years=year)

with open(str(year) + ".csv", "w", newline='', encoding='UTF8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Salary date", "Accountant message date"])

    for month in range(1, 13):

        day = 10
        date = datetime.date(year, month, day)
        while date.weekday() > 4 or date in holidays:
            day -= 1
            date = datetime.date(year, month, day)

        csv_writer.writerow([date, date - datetime.timedelta(3)])
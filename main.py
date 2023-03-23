"""SPINTEK kodutöö Karl Erik Seeder 23.03.2023"""
import csv
import datetime
import sys

import holidays


class Homework:
    """
    In the company people get paid on the 10th,

    people can only get paid during a workday,
    therefore if the payday falls onto an event(EG independence day)
    or weekend then the person will get paid on the previous workday
    The accountant would love to be notified/reminded 3 days before the payday

    1. The task should be to make a CLI function, which takes an input (parameter - year)
    and outputs a table, where there is a date of the payday and reminder to the accountant
    (should be 12 lines in total and the table header)
    2. The function has to write a CSV file (eg. 2023.csv)
    """

    def __init__(self, year: int):
        """
        Constructor for Homework
        :param year:  Year to base the table for
        """
        # Day-Month-Year Variables
        self.day = 10
        self.month = 1  # January
        self.year = year  # Year to base the table for
        self.JANUARY_MONTH = 1  # Final value
        self.DECEMBER_MONTH = 12  # Final value
        # Lists
        self.work_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.weekends = ["Saturday", "Sunday"]
        self.holidays = holidays.EE(years=self.year)
        # Dates
        self.current_date = datetime.date(self.year, self.month, self.day)  # format year, month, day
        self.dt = datetime.timedelta(3)
        self.accountant_date = self.current_date - self.dt
        # CSV file variables
        self.csv = []

    def update_values(self) -> None:
        """Method to update the dates value"""
        self.current_date = datetime.date(self.year, self.month, self.day)  # format year, month, day
        self.accountant_date = self.current_date - self.dt

    def get_day_string(self) -> datetime:
        """Getter for the current day (Mon-Sun)"""
        return self.current_date.strftime("%A")

    def get_accountant_day_string(self) -> datetime:
        """Getter for the accountants date (day-month-day number)"""
        return self.accountant_date.strftime("%A")

    def get_date_string(self) -> datetime:
        """Getter for the current date string (day-month-day number)"""
        return self.current_date.strftime("%A, %B %d")

    def get_accountant_date_string(self) -> datetime:
        """Getter for the accountants date (day-month-day number)"""
        return self.accountant_date.strftime("%A, %B %d")

    def move_to_next_month(self) -> None:
        """Method to go to the next month"""
        self.month += 1
        self.day = 10
        self.update_values()

    def go_back_a_day(self) -> None:
        """Method to check if the following salary day is a special day, move the day back by 1"""
        self.day -= 1
        self.update_values()

    def is_workday(self) -> bool:
        """Method to check if given day is a work day or not"""
        return self.get_day_string() in self.work_days

    def is_holiday(self) -> bool:
        """Method to check if its a holiday or not"""
        return self.current_date in self.holidays

    def is_accountant_workday(self) -> bool:
        """Method to check if given day is a work day or not"""
        return self.get_accountant_day_string() in self.work_days

    def is_accountant_holiday(self) -> bool:
        """Method to check if the day is a holiday or not"""
        return self.accountant_date in self.holidays

    def calculate_dates(self) -> None:
        """Method which calculates the Workers salary date and the accountants notification date"""
        date_list = []
        while not self.is_workday() and not self.is_holiday():
            self.go_back_a_day()
        date_list.append(self.get_date_string())
        while not self.is_accountant_workday() and not self.is_accountant_holiday():
            self.go_back_a_day()
        date_list.append(self.get_accountant_date_string())
        self.csv.append(date_list)  # Add date to list


    def make_table(self) -> None:
        """Method to fill list with appropriate dates"""
        for month in range(self.JANUARY_MONTH, self.DECEMBER_MONTH + 1):# Add +1 cause range does not include last int
            self.calculate_dates()
            if month < self.DECEMBER_MONTH:  # If it's not December move on to the next month
                self.move_to_next_month()

    def write_csv_file(self) -> None:
        """Function to write CSV file"""
        print(self.csv)
        # Writes csv file
        with open(str(year)+".csv", "w", newline='', encoding='UTF8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["Salary date", "Accountant message date"])
            for k in self.csv:
                csv_writer.writerow(k)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        year = int(sys.argv[1])
    else:
        print("Error, parameter year not defined")
        exit(1)
    homework = Homework(year)
    print(homework.make_table())
    homework.write_csv_file()
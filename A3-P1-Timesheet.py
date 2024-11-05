"""
    Title:  Program 1 - Timesheet
    Author: Dan Shaw w0190983
    Description: Design and write a program that accepts the number of hours worked on each of five work days from the user, then displays different information calculated about those entries as output. 
"""

from operator import indexOf
import ds_tower as tower

MAX_HOURS = 24
MAX_DAYS = 7

def main():
    title = "Timesheet Calculator"

    # Outputs the MOTD using ds_tower's Template class
    print(tower.Template.titleOut(title))
    hours = getHoursForWeek()
    highestHours = calculateMaxHours(hours)
    totalHours = calculateTotalHours(hours)
    averageHours = calculateAverageHours(hours)

    print("The highest amount of hours worked was {0} on the following days: ".format(highestHours[0]))
    for i in range(len(highestHours[1])):
        print("Day {0}".format(highestHours[1][i]))

def calculateInsufficientHours(hours:list):
    pass

def calculateTotalHours(hours:list):
    return sum(hours)

def calculateAverageHours(hours:list):
    return (sum(hours) / len(hours))

def calculateMaxHours(hours:list):
    """Returns the highest number of hours worked in a week, and a list of the days that number was worked"""
    highest = max(hours)
    days = []

    for i in range(len(hours)):
        if hours[i] == highest:
            days.append(i + 1)

    return highest, days

def getHoursForWeek(daysPerWeek:int = 5):
    """Returns a list of hours worked for each day of the week, using daysPerWeek as the length of your work week"""
    hours = []
    for i in range(daysPerWeek):
        print("Enter hours for day {0}".format(i + 1))
        hours.append(getHoursForDay())

    return hours

def getHoursForDay():
    """Returns the number of hours worked for a single day"""
    daily = tower.Validator.inputAndValidateFloat("> ")

    return daily

if __name__ == "__main__":
    main()
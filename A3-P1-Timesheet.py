"""
    Title:  Program 1 - Timesheet
    Author: Dan Shaw w0190983
    Description: Design and write a program that accepts the number of hours worked on each of five work days from the user, then displays different information calculated about those entries as output. 
"""

import ds_tower as tower

MAX_HOURS = 24
MAX_DAYS = 7

class WeekStats:
    # Passing 5 variables around as local variables one-by-one was getting cumbersome so I encapsulated them into a WeekStats object so I can just move that
    def __init__(self, hours:list[int], highestHours:list[list], totalHours:int, averageHours:int, insufficientHours:list[list]):
        WeekStats.hours = hours
        WeekStats.highestHours = highestHours
        WeekStats.totalHours = totalHours
        WeekStats.averageHours = averageHours
        WeekStats.insufficientHours = insufficientHours

def main():
    title = "Timesheet Calculator"

    # Outputs the MOTD using ds_tower's Template class
    print(tower.Template.titleOut(title))
    hours = getHoursForWeek()
    weekStats = WeekStats(hours, getMaxHours(hours), getTotalHours(hours), getAverageHours(hours), getInsufficientHours(hours))

    outputResults(weekStats)

def outputResults(weekStats):
    """Outputs the results of the timesheet calculations"""
    print("Hours worked: {0}".format(weekStats.hours))
    print("Total hours worked: {0}".format(weekStats.totalHours))
    print("Average hours worked: {0}".format(weekStats.averageHours))
    print("Days with insufficient hours worked: {0} with hours {1}".format(weekStats.insufficientHours[1], weekStats.insufficientHours[0]))
    print("Highest number of hours worked: {0} on days {1}".format(weekStats.highestHours[0], weekStats.highestHours[1]))

def getInsufficientHours(hours:list[int]):
    """Returns a list of hours worked that are less than 7"""
    """
        NOTE First time using List Comprehension! I learned something new. I know this is the loops & lists assignment but this is too slick not to use.
        Although I guess List Comprehension is sort of a loop on its own, so I'll defend the usage with that.
        
        Just for posterity though, the normal loop would have been something like:

        for i in range(len(hours)):
            if hours[i] < 7:
                days.append(i + 1)
                insufficientHours.append(hours[i])
    """
    insufficientHours = [[x for x in range(1, len(hours) + 1) if hours[x - 1] < 7], # First list stores the days with insufficient hours
                         [x for x in hours if x < 7]]                               # Second list stores the hours worked on those days

    return insufficientHours

def getTotalHours(hours:list[int]):
    return sum(hours)

def getAverageHours(hours:list[int]):
    return (sum(hours) / len(hours))

def getMaxHours(hours:list[int]):
    """Returns the highest number of hours worked in a week, and a list of the days that number was worked"""
    """
        I'm keeping the loop in this time in favour of the list comprehension because I have to hit those assignment outcomes somewhere
        
        But I'd strongly rather use:
            days = [x for x in range(1, len(hours) + 1) if hours[x - 1] == highest]

    """
    days = []
    highest = max(hours)
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

    # Requires the user to enter a float between the range of 0 and 24
    while (daily := tower.Validator.inputAndValidateFloat("> ")) < 0 or daily > MAX_HOURS:
        print("Invalid input. Please enter a number between 0 and {0}".format(MAX_HOURS))

    return daily

if __name__ == "__main__":
    main()
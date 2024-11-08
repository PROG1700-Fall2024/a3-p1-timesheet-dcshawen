"""
    Title:  Program 1 - Timesheet
    Author: Dan Shaw w0190983
    Description: Design and write a program that accepts the number of hours worked on each of five work days from the user, then displays different information calculated about those entries as output. 
"""

import ds_tower1_3_0 as tower

MAX_HOURS = 24
MAX_DAYS = 7
INS_THRESH = 7

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
    instr = "To calculate your timesheet, first enter the number of days you worked this week (Default 5 if nothing is entered)."

    # Outputs the MOTD using ds_tower's Template class
    print(tower.Template.titleOut(title))
    print(instr)
    while (dayCount := tower.Validator.inputAndValidateInt(tower.PROMPT, "Invalid Input", [None])) > MAX_DAYS:
        print("Invalid input. Please enter a number between 1 and {0}".format(MAX_DAYS))
    
    if dayCount == 0:
        print("Then why are you here?")
        exit()
        
    instr = "Next, enter the number of hours you worked each day."
    hours = getHoursForWeek(dayCount)
    weekStats = WeekStats(hours, getMaxHours(hours), getTotalHours(hours), getAverageHours(hours), getInsufficientHours(hours))

    outputResults(weekStats)

def outputMostHours(weekStats):
    if (len(weekStats.highestHours[1]) > 1):
        highestStr = "There were multiple days with the highest hours."
    else:
        highestStr = "There was only one day with the highest hours worked."
    print(highestStr)
    for i in range(len(weekStats.highestHours[1])):
        print("Day {0}: {1} hours".format(weekStats.highestHours[1][i], str(weekStats.highestHours[0]).strip(".0")))

def outputTotalHours(weekStats):
    print("Total Number of Hours Worked: {0}".format(str(weekStats.totalHours).strip(".0")))

def outputAverageHours(weekStats):
    print("Average number of hours worked each day: {0:.1f}".format(weekStats.averageHours))

def outputInsufficientHours(weekStats):
    if (len(weekStats.insufficientHours[0]) > 1):
        insufficientStr = "There were multiple days with insufficient hours."
    else:
        insufficientStr = "There was only one day with insufficient hours."    
    print(insufficientStr)
    for i in range(len(weekStats.insufficientHours[0])):
        print("Day {0}: {1} hours".format(weekStats.insufficientHours[0][i], str(weekStats.insufficientHours[1][i]).strip(".0")))

def outputResults(weekStats):
    """Outputs the results of the timesheet calculations"""
    resultStr = "Timesheet Results"
    daysWorkedStr = "Summary of hours worked for the week"
    print(tower.Template.titleOut(resultStr))

    outputMostHours(weekStats)
    print(tower.Template.getLine('-'))
    outputTotalHours(weekStats)
    outputAverageHours(weekStats)
    print(tower.Template.getLine('-'))
    outputInsufficientHours(weekStats)

def getInsufficientHours(hours:list[int]):
    """Returns a list of hours worked that are less than 7"""
    """
        NOTE First time using List Comprehension! I learned something new. I know this is the loops & lists assignment but this is too slick not to use.
        Although I guess List Comprehension is sort of a loop on its own, so I'll defend the usage with that.
        
        Just for posterity though, the normal loop would have been something like:
    
    def getInsufficientHours(hours:list[int]):
        for i in range(len(hours)):
            if hours[i] < 7:
                days.append(i + 1)
                hours.append(hours[i])
        return [ days, hours ]
    """
    insufficientHours = [[x for x in range(1, len(hours) + 1) if hours[x - 1] < INS_THRESH], # First list stores the days with insufficient hours
                         [x for x in hours if x < INS_THRESH]]                               # Second list stores the hours worked on those days

    return insufficientHours

def getTotalHours(hours:list[int]):
    return sum(hours)

def getAverageHours(hours:list[int]):
    return (sum(hours) / len(hours))

def getMaxHours(hours:list[int]):
    """Returns the highest number of hours worked in a week, and a list of the days that number was worked"""
    """
        I'm keeping the loop in this time in place of the list comprehension because I have to hit those assignment outcomes somewhere
        
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
    while (daily := tower.Validator.inputAndValidateFloat(tower.PROMPT)) < 0 or daily > MAX_HOURS:
        print("Invalid input. Please enter a number between 0 and {0}".format(MAX_HOURS))

    return daily

if __name__ == "__main__":
    main()
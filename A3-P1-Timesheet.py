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
    def __init__(self, hours:list[int]):
        WeekStats.hours = hours
        WeekStats.highestHours = WeekStats.setHighestHours(self, hours)
        WeekStats.totalHours = WeekStats.setTotalHours(self, hours)
        WeekStats.averageHours = WeekStats.setAverageHours(self, hours)
        WeekStats.insufficientHours = WeekStats.setInsufficientHours(self, hours)

    def setHighestHours(self, hours):
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
    
    def setTotalHours(self, hours):
        """Returns the total number of hours worked in a week"""
        return sum(hours)
    
    def setAverageHours(self, hours):
        """Returns the average number of hours worked in a week"""
        return (sum(hours) / len(hours))
    
    def setInsufficientHours(self, hours):
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

def main():
    title = "Timesheet Calculator"
    instr = "To calculate your timesheet, enter the number of hours you worked each day of a 5 day work week."
    # Outputs the MOTD using ds_tower's Template class
    print(tower.Template.titleOut(title))
    print(instr)
       
    hours = getHoursForWeek()
    weekStats = WeekStats(hours)

    outputResults(weekStats)

def outputMostHours(weekStats):
    if weekStats.totalHours == 0:
        print("You didn't work any hours this week.")
        return
    
    if (len(weekStats.highestHours[1]) > 1):
        highestStr = "There were multiple days with the highest hours worked:"
    elif (len(weekStats.highestHours[1]) == 0):
        highestStr = "I don't think this line is even reachable through normal operations, Geoff, but I'm leaving it in just in case you find a way."
    else:
        highestStr = "There was only one day with the highest hours worked:"
    print(highestStr)

    for i in range(len(weekStats.highestHours[1])):
        if weekStats.highestHours[0] % 10 == 0: # Checks for trailing 0s before the decimal place. Relying on only .strip() was producing some weird results
            print("Day {0}: {1:.0f} hours".format(weekStats.highestHours[1][i], weekStats.highestHours[0]))
        else:
            print("Day {0}: {1} hours".format(weekStats.highestHours[1][i], str(weekStats.highestHours[0]).strip(".0")))

def outputTotalHours(weekStats):
    if weekStats.totalHours == 0 or weekStats.totalHours % 10 == 0:
        print("Total Number of Hours Worked: {0:.0f}".format(weekStats.totalHours))
    else:
        print("Total Number of Hours Worked: {0}".format(str(weekStats.totalHours).strip(".0")))

def outputAverageHours(weekStats):
    print("Average number of hours worked each day: {0:.1f}".format(weekStats.averageHours))

def outputInsufficientHours(weekStats):
    if (len(weekStats.insufficientHours[0]) > 1):
        insufficientStr = "There were multiple days with insufficient hours worked:"
    elif (len(weekStats.insufficientHours[0]) == 0):
        insufficientStr = "All days had sufficient hours worked."
    else:
        insufficientStr = "There was only one day with insufficient hours worked:"    
    print(insufficientStr)
    for i in range(len(weekStats.insufficientHours[0])):
        if weekStats.insufficientHours[1][i] == 0:
            print("Day {0}: {1:.0f} hours".format(weekStats.insufficientHours[0][i], weekStats.insufficientHours[1][i]))
        else:
            print("Day {0}: {1} hours".format(weekStats.insufficientHours[0][i], str(weekStats.insufficientHours[1][i]).strip(".0")))

def outputResults(weekStats):
    """Outputs the results of the timesheet calculations"""
    resultStr = "Timesheet Results"

    print(tower.Template.titleOut(resultStr))

    outputMostHours(weekStats)
    print(tower.Template.getLine('-'))
    outputTotalHours(weekStats)
    outputAverageHours(weekStats)
    print(tower.Template.getLine('-'))
    outputInsufficientHours(weekStats)

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
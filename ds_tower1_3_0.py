"""
    Author: Dan Shaw
    Title: DS Tower
    Desc: Contains custom math and validation functions
"""

PROMPT = ">: "

class Validator:
    """ Custom math functions """
    defaultErrorString = "Invalid input"

    def validateFloat(inputQuery:str):
        """ Validates whether inputQuery is a valid FLOAT. Returns converted FLOAT if successful. Returns None if fails. """
        try:
            return float(inputQuery)
        except:
            return None

    def validateInt(inputQuery:str):
        """ Validates whether inputQuery is a valid INT. Returns converted INT if successful. Returns None if fails. """
        
        try:
            return int(inputQuery)
        except:
            return None

    def inputAndValidateInt(outputString:str, errorString:str = defaultErrorString):
        """ Forces user to enter a INT value before continuing. Returns an integer. """
        
        while (inputString := Validator.validateInt(input(outputString))) == None:
            print(errorString)

        return int(inputString)
        
    def inputAndValidateFloat(outputString:str, errorString:str = defaultErrorString):
        """ Forces user to enter a FLOAT before continuing. Returns a float. """
        while (inputString := Validator.validateFloat(input(outputString))) == None:
            print(errorString)    

        return float(inputString)
    
class Template:
    def titleOut(title:str, d:chr = "-"):
        """ Returns title formatted as a banner, using d as the decorative character """
        return "{0}\n| {1} |\n{0}".format(d * (len(title) + 4), title)
    
    def getLine(c:str = "*"):
        """ Prints a line of characters """
        return (c * 50)
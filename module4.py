from math import pi as p

def squareFoot():
    length = int(input("What is the length of the house? "))
    width = int(input("What is the width of the house? "))

    area = length * width

    returnText = "The house's square footage is " + str(area)

    return returnText

    

def circleCircumference():
    radius = int(input("What is the radius of the circle? "))

    circumference = round(2 * p * radius)

    return "The circumference is " + str(circumference)



    

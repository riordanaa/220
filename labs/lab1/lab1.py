"""
Name: <Aidan Riordan>
program name: <lab1.py>
lab1.py
Problem: This function calculates the area of a rectangle
"""
print("I look forward to learning to control this computer through programming!")

def calc_area():
    length = 20
    width = 5
    area = length * width
    print("Area =", area)

def calc_rec_area():
    length=eval(input("what is the length?"))
    width=eval(input("what is the width?"))
    area = length * width
    print("Area =", area)

def calc_volume():
    length=eval(input("what is the length?"))
    width=eval(input("what is the width?"))
    height=eval(input("what is the height?"))
    volume = length*width*height
    print("volume =",volume)

def shooting_percentage():
    shots_made=eval(input("How many shots did the player make?"))
    total_shots=eval(input("How many total shots were there?"))
    shooting_percentage= shots_made/total_shots
    print("shooting percentage=",shooting_percentage*100,"%")

def coffee():
    lbs_coffee_purchased=eval(input("How many pounds of coffee are purchased?"))
    total_cost= 10.5*lbs_coffee_purchased+.86*lbs_coffee_purchased+1.5
    print("the total cost is",total_cost,"$")

def kilometers_to_miles():
    miles=eval(input("How many miles will you travel?"))
    kilometers= miles/1.61
    print(miles,"miles =",kilometers,"kilometers")

kilometers_to_miles()
coffee()
shooting_percentage()
calc_rec_area()
calc_volume()
calc_area()

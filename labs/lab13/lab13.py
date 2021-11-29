"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""
def binary_search(value,lst):
    left = 0
    right = len(lst)-1
    while left <= right:
        middle = (right + left)//2
        middle_value = lst[middle]
        if value == middle_value:
            return True
        if value < middle_value:
            right = middle-1
        if value > middle_value:
            left = middle + 1
    return False

def selection_sort(values):

    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i+1, len(values)):
            if values[j] < values[i]:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]

def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    return dy*dx





def rect_sort(rects):
    dict = {}
    areas = []
    for rect in rects:
        dict[calc_area(rect)] = rect
        areas.append(calc_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rects[i] = dict[areas[i]]

#capstone 2
#find 5 numbers that fall in this range 4000-5000 inclusive
def star_find(filename):
    infile = open(filename, "r")
    contents = infile.read()
    found_signals = []
    signals = contents.split() #this is a list of strings we need int
    last_pos = 0
    for i in range(len(signals)):
        if int(signals[i]) >=4000 and int(signals[i]) <=5000:
            found_signals.append(int(signals[i]))
        if len(found_signals) == 5:
            last_pos = i
            break
    print("There are " + str(len(found_signals)) + "signals")
    print("Here are the signals we found:" + str(found_signals))
    if len(found_signals) < 5:
        print("we didnt find 5 signals, so there is not a neutron star")
    else:
        print("The last position of the last signal we found was:" + str(last_pos))
#compare current signal with acceptable range
# if in the range, add the signal to a new list of signals
#if we found 5 signals stop the loop len
#print number of signals len(found_signals)
#print found_signals
#if we didnt find 5 signals:
#print("we didnt find 5")
#else:
#print last position (you will need an itterater i to keep track of where you are)

def main():
    # add other function calls here
    pass


main()

'''
Name: <Aidan Riordan>
program name: <traffic.py>
problem: Help analyze trafic patterns
I Aidan Riordan certify that this is my own work
'''

def main():
    num_roads_surveyed = int(input("How many roads were surveyed?"))
    days = []
    bigger_acc = 0
   # acc_total_num_viacles
    for road in range (num_roads_surveyed):
        days = int(input("How many days was road " + str(road+1) + " surveyed?"))
        acc = 0

        for day in range (days):

            cars = int(input("How many cars traveled on day " + str(day+1) + "?"))
            acc = acc + cars
            avg_per_day = acc/days
        bigger_acc = bigger_acc + acc
            # we need a total number of roads

            # we need a total number of all viacles
        print("Road " + str(road+1) + " average vehicles per day:" + str(avg_per_day))
            # output avg num vehicles traveled down each road per day and
    print("The total number of vehicles traveled on all roads:" + str(bigger_acc))
    print("Average number of vehicles per road:" + str(round(bigger_acc/num_roads_surveyed,2)))
    # total viacles and avg vehicles for all roads

if __name__ == '__main__':
    main()

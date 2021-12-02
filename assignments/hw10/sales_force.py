"""
Name: <Aidan Riordan>
program name: <salesforce.py>
I Aidan Riordan certify that this is my own work
"""
from sales_person import SalesPerson


class SalesForce:
    """This class manages a salesforce"""

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, "r")
        for line in file.readlines():
            employee_id, name, sales = line.split(",")
            unique_object_name = "employee" + str(employee_id)
            unique_object_name = SalesPerson(employee_id, name)
            sales = sales.split()
            for sale in sales:
                unique_object_name.enter_sale(sale)
            self.sales_people.append(unique_object_name)
        file.close()

    def quota_report(self, quota):
        list_a = []
        for person in self.sales_people:
            sublist = [int(person.get_id()), person.get_name(), person.total_sales(), person.met_quota(quota)]
            list_a.append(sublist)
        return list_a

    def top_seller(self):
        people_highest_total_sales = []
        total_sales = []
        for person in self.sales_people:
            if not person.total_sales():
                total_sales.append(0)
            else:
                total_sales.append(person.total_sales())
        highest_total = 0
        for i in range(len(total_sales)):
            if total_sales[i] >= highest_total:
                people_highest_total_sales.append(self.sales_people[i])
        return people_highest_total_sales

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if person.get_id() == employee_id:
                return person
        return None
        # do i need to convert to int or string here? line 26.

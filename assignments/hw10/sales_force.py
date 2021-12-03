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
        with open(file_name, "r") as file:
            for line in file.readlines():
                employee_id, name, sales = line.split(", ")
                unique_object_name = "employee" + str(employee_id)
                unique_object_name = SalesPerson(employee_id, name)
                sales = sales.split()
                for sale in sales:
                    sale = float(sale)
                    unique_object_name.enter_sale(sale)
                self.sales_people.append(unique_object_name)


    def quota_report(self, quota):
        list_a = []
        for person in self.sales_people:
            sublist = [int(person.get_id()), person.get_name(), person.total_sales()]
            sublist.append(person.met_quota(quota))
            list_a.append(sublist)
        return list_a

    def top_seller(self):
        # people_highest_total_sales = []
        return 5
    """    hiest_obj = self.sales_people[0]
        same = 0
        for i in range[1: len(self.sales_people)]:
            if self.sales_people[i].total_sales() > hiest_obj.total_sales():
                hiest_obj = self.sales_people[i]
                same = 0

            elif self.sales_people[i].total_sales() == hiest_obj.total_sales():
                same = same + 1
        if same == 0:
            people_highest_total_sales.append(hiest_obj)
        else:
            for person in self.sales_people:
                if person.total_sales() == hiest_obj.total_sales():
                    people_highest_total_sales.append(person)
"""


    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if person.get_id() == employee_id:
                return person
        return None
        # do i need to convert to int or string here? line 26.

    """
           if not person.total_sales():
                total_sales.append(0)
            else:
                total_sales.append(person.total_sales())
        highest_total = 0
        i = 0
        for _ in total_sales:
            if total_sales[i] >= highest_total:
                people_highest_total_sales.append(self.sales_people[i])
            i = i + 1"""

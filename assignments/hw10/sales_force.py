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
        top_seller = []
        highest_total_sales = self.sales_people[0].total_sales()
        for person in self.sales_people:
            if person.total_sales() > highest_total_sales:
                highest_total_sales = person.total_sales()

        for person in self.sales_people:
            if person.total_sales() == highest_total_sales:
                top_seller.append(person)
        return top_seller

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if person.get_id() == employee_id:
                return person
        return None

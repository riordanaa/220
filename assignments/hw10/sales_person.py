"""
Name: <Aidan Riordan>
program name: <salesperson.py>
I Aidan Riordan certify that this is my own work
"""
class SalesPerson:
    """This class contains employee data on a respective sales person"""

    def __init__(self, employee_id, name):
        """Initializes the sales person with respective employee_id and name"""
        self.employee_id = int(employee_id)
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        acc = 0
        for sale in self.sales:
            acc = acc + sale
        return acc

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return -1
        if self.total_sales() > other.total_sales():
            return 1
        return 0

    def __str__(self):
        return "{0}-{1}:{2}".format(str(self.get_id()), self.get_name(), str(self.total_sales()))

# note when do we need to change the data types in order to pass the tests?
# when they are entered? when they are got by getters?
# made in a class function.

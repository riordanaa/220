class SalesPerson:
    """This class contains employee data on a respective sales persond"""

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
        if self.total_sales() >= quota: # When do we put () to call a function? allways!
            return True
        return False

    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return -1
        if self.total_sales() > other.total_sales():
            return 1
        return 0


    def __str__(self):
        x = "{0}-{1}:{2}".format(str(self.get_id()), self.get_name(), str(self.total_sales()))
        return x










#note when do we need to change the data types in order to pass the tests??
# when they are entered? when they are got by getters?

# on line 24, do you want me to call it from the instance variable or from the getter function? This reference is being
#made in a class function.



#below testing the string formatting
"""employee_1 = SalesPerson(201, "aidan")
print(employee_1.get_name())
employee_1.enter_sale(10)
employee_1.enter_sale(20)
print(employee_1.__str__())"""
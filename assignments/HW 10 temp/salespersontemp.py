class SalesPerson:
    """This class contains employee data on a respective sales person"""

    def __init__(self,employee_id,name):
        """Initializes the sales person with respective employee_id and name"""
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return int(self.employee_id)

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

    def get_sales(self):
        return self.sales


#note when do we need to change the data types in order to pass the tests??
# when they are entered? when they are got by getters?
class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)

    def set_given_name(self, given_name):
        self.given_name = given_name

    def set_family_name(self, family_name):
        self.family_name = family_name

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

customer1 = Customer("George", "Odhiambo")
customer2 = Customer("John", "Maina")
customer3 = Customer("David", "Ndiba")
customer4 = Customer("Nahashon", "Waichai")
customer5 = Customer("Newton", "Jenga")

#update customer
customer1.set_given_name("Derrick")
customer2.set_family_name("Ojongo")


print(customer1.given_name())  
print(customer2.family_name()) 
print(customer1.full_name())   


all_customers = Customer.all()
for customer in all_customers:
    print(customer.full_name())

class Customer:
    def __init__(self, n, a,):
        self.name = n
        self.age = a
        self.products = []

    def __str__(self):
        return(f"This is  name {self.name} and age {self.age} ")

    def birth_date(self,curr_year):
        return(curr_year - self.age)

    def add_product(self, title):
        self.products.append(title)

user1 = Customer("Petya", 25)
user2 = Customer("Roma", 24)
# user2.add_product("Coke")
# user1.add_product("Bread")

# print(user1.products)
# print(user2.products)
customers = []
customers.append(user1)
customers.append(user2)

print(customers[0].name)

for c in customers:
    print(c.name, c.age)

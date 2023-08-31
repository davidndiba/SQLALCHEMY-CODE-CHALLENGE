class Restaurant:
    def __init__(self, name):
        self.name = name  
    def get_name(self):
        return self.name


restaurant = Restaurant("Kitchen f'cs")


print(restaurant.get_name()) 

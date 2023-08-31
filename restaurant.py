class Restaurant:
    def __init__(self, name):
        self._name = name  
    def get_name(self):
        return self._name


restaurant = Restaurant("Kitchen f'cs")

print(restaurant.get_name()) 

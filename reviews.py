class Review:
    all_reviews = [] 
    
    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all_reviews.append(self)  

    def rating(self):
        return self._rating

    @classmethod
    def all(cls):
        return cls.all_reviews

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant


class Customer:
    def __init__(self, name):
        self._name = name
        self._reviews = []

    def name(self):
        return self._name

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self._reviews.append(new_review)

        

    def restaurants(self):
        reviewed_restaurants = set()
        for review in self._reviews:
            reviewed_restaurants.add(review.restaurant())
        return list(reviewed_restaurants)
    

    def num_reviews(self):
        return len(self._reviews),

    
     @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        matching_customers = []
        for customer in cls.all_customers:
            if customer.name().split()[0] == name:
                matching_customers.append(customer)
        return matching_customers



class Restaurant:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    def reviews(self):
        restaurant_reviews = []
        for review in Review.all():
            if review.restaurant() == self:
                restaurant_reviews.append(review)
        return restaurant_reviews

    def customers(self):
        reviewed_customers = set()
        for review in self.reviews():
            reviewed_customers.add(review.customer())
        return list(reviewed_customers)

def average_star_rating(self):
        total_ratings = sum(review.rating() for review in self.reviews())
        num_reviews = len(self.reviews())
        if num_reviews == 0:
            return 0
        return total_ratings / num_reviews

#instance
customer1 = Customer("George")
customer2 = Customer("John")

restaurant1 = Restaurant("Kitchen f'cs")
restaurant2 = Restaurant("Pizza Paradise")


customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 3)
customer2.add_review(restaurant1, 5)


print("Restaurant 1 Reviews:", [review.rating() for review in restaurant1.reviews()])  
print("Restaurant 1 Customers:", [customer.name() for customer in restaurant1.customers()])  
print("Customer 1 Reviewed Restaurants:", [restaurant.name() for restaurant in customer1.restaurants()])  

print("Customer 1 Total Reviews:", customer1.num_reviews())  

found_customer = Customer.find_by_name("George")
if found_customer:
    print("Found Customer:", found_customer.name()) 
all_bobs = Customer.find_all_by_given_name("George")
print("All Bobs:", [customer.name() for customer in all_bobs])  
print("Restaurant 1 Average Star Rating:", restaurant1.average_star_rating())  
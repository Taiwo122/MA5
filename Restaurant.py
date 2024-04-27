# Define a class called Restaurant.
class Restaurant:
    # Initialize the Restaurant class with restaurant_name and cuisine_type attributes.
    def __init__(self, restaurant_name, cuisine_type):
        # Store the attributes passed during initialization.
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # Method to describe the restaurant by printing its name and cuisine type.
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    # Method to print a message indicating that the restaurant is open.
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

# Create an instance of Restaurant called restaurant.
restaurant = Restaurant("The Food Place", "Italian")
# Print the restaurant's attributes individually.
print(f"Restaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")
# Call the describe_restaurant() method.
restaurant.describe_restaurant()
# Call the open_restaurant() method.
restaurant.open_restaurant()

# Create three instances of Restaurant and call describe_restaurant() for each instance.
restaurant1 = Restaurant("Burger Joint", "American")
restaurant2 = Restaurant("Sushi Corner", "Japanese")
restaurant3 = Restaurant("Taco House", "Mexican")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# Define a class called User with first_name, last_name, age, email attributes.
class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    # Method to describe the user by printing their information.
    def describe_user(self):
        print(f"User Information:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    # Method to print a personalized greeting to the user.
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome.")

# Create an instance of User and call describe_user() and greet_user().
user1 = User("John", "Doe", 30, "john.doe@email.com")
user1.describe_user()
user1.greet_user()

# Define the Restaurant class with an additional number_served attribute and related methods.
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Adding the number_served attribute with default value 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Number Served: {self.number_served}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, number):
        self.number_served = number  # Method to set the number of customers served

    def increment_number_served(self, increment):
        self.number_served += increment  # Method to increment the number of customers served

# Create an instance of Restaurant and demonstrate changing number_served.
restaurant = Restaurant("The Food Place", "Italian")
restaurant.describe_restaurant()  # Print initial number of customers served

restaurant.number_served = 50  # Change the value directly
restaurant.describe_restaurant()  # Print updated number of customers served

restaurant.set_number_served(100)  # Use set_number_served method
restaurant.describe_restaurant()  # Print updated number of customers served

restaurant.increment_number_served(20)  # Incrementing number served
restaurant.describe_restaurant()  # Print incremented number of customers served

# Define the User class with an additional login_attempts attribute and related methods.
class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0  # Adding login_attempts attribute with default value 0

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1  # Method to increment login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0  # Method to reset login_attempts

# Create an instance of User and demonstrate incrementing and resetting login_attempts.
user = User("John", "Doe", 30, "john.doe@email.com")
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login Attempts: {user.login_attempts}")  # Check incremented value

user.reset_login_attempts()
print(f"Login Attempts after reset: {user.login_attempts}")  # Check reset value

# Define a class called IceCreamStand that inherits from Restaurant.
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("Available Ice Cream Flavors:")
        for flavor in self.flavors:
            print(flavor)

# Create an instance of IceCreamStand and call display_flavors().
ice_cream_flavors = ["Vanilla", "Chocolate", "Strawberry"]
ice_cream_stand = IceCreamStand("Scoops & Smiles", "Ice Cream", ice_cream_flavors)
ice_cream_stand.display_flavors()

# Define a class called Admin that inherits from User and adds privileges attribute and related methods.
class Admin(User):
    def __init__(self, first_name, last_name, age, email, privileges):
        super().__init__(first_name, last_name, age, email)
        self.privileges = privileges

    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(privilege)

# Create an instance of Admin and demonstrate show_privileges().
admin_privileges = ["can add post", "can delete post", "can ban user"]
admin_user = Admin("Admin", "User", 40, "admin@example.com", admin_privileges)
admin_user.show_privileges()

# Define a separate Privileges class and move show_privileges() method to it.
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(privilege)

# Create a Privileges instance and use it as an attribute in Admin class.
privileges_instance = Privileges(admin_privileges)
admin_user_with_privileges = Admin("Admin", "WithPrivileges", 35, "admin@example.com", privileges_instance)
admin_user_with_privileges.show_privileges()

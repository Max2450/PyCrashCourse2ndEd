class Restaurant:
    """A class for modeling restaurants."""

    def __init__(self, name, cuisine):
        """Initialize a restaurant, saving the name and cuisine."""
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Describe a restaurant using the name and cuisine type."""
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        """Open the restaurant."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, new_number_served):
        self.number_served = new_number_served

    def increment_number_served(self, more_served):
        if (more_served > 0):
            self.number_served += more_served
        else:
            print(f"We can't serve less than 1 person!")
class Restaurant:
    """A class for modeling restaurants."""

    def __init__(self, name, cuisine):
        """Initialize a restaurant, saving the name and cuisine."""
        self.restaurant_name = name
        self.cuisine_type = cuisine

    def describe_restaurant(self):
        """Describe a restaurant using the name and cuisine type."""
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        """Open the restaurant."""
        print(f"{self.restaurant_name} is now open!")
class User:
    """A class for modeling users"""

    def __init__(self, first_name, last_name, age, email, password, pic):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password
        self.pic = pic
        self.login_attempts = 0

    def describe_user(self):
        print(f"This user's information is as follows: "
              f"{self.first_name, self.last_name, self.age, self.email, self.password, self.pic}")

    def greet_user(self):
        print(f"Hello there {self.first_name}! ")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin (User):
    """Model Admins as a subclass of users with additional privileges"""

    def __init__(self, *privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"This Admin's privileges are: {self.privileges}.")
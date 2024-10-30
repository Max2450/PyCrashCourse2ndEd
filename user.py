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

class Admin2(User):
    """Model an Admin with privileges as a separate class for 9-8"""

    def __init__(self, *privileges):
        self.privileges = Privileges()

class Privileges():
    """Alternate way to handle privileges outside of the user class for 9-8"""

    def __init__(self, *privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"Using a Privileges instance as an attribute of Admin2, this user's privileges are: {self.privileges}")

class User:
    """A class for modeling users"""

    def __init__(self, first_name, last_name, age, email, password, pic):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password
        self.pic = pic

    def describe_user(self):
        print(f"This user's information is as follows: "
              f"{self.first_name, self.last_name, self.age, self.email, self.password, self.pic}")

    def greet_user(self):
        print(f"Hello there {self.first_name}! ")
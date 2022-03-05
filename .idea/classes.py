import datetime

class User:
    pass

user1=User()
user1.first_name="John"
user1.last_name="Doe"
print(user1.first_name, user1.last_name)
user2=User()
user2.first_name="Max"
user2.last_name="Mustermann"

print(user2.first_name, user2.last_name)

class UserFull:
    """This class is created to define the main information of users"""
    def __init__(self, full_name, birthday):
        self.name=full_name
        self.birthday=birthday #yyyymmdd
        name_pieces=full_name.split(" ")
        self.first_name=name_pieces[0]
        self.last_name=name_pieces[-1]
    def age(self):
        """Returns the age of the user in years."""
        today=datetime.date(2022,3,3)
        yyyy=int(self.birthday[0:4])
        dd=int(self.birthday[4:6])
        mm=int(self.birthday[6:8])
        dob=datetime.date(yyyy,mm,dd)
        age_in_days=(today-dob).days
        age_in_years=age_in_days/365
        return int(age_in_years)
user=UserFull("Johnny Doe","19760102")
print(user.name, user.birthday)
print(user.first_name, user.last_name)
help(UserFull)
user3=UserFull("Max Mustermann","19760201")
print(user3.age())
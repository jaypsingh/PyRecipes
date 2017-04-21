'''
This program demonstrates a simple example of how we can short the objects of a class using a buit in method 'sorted'
'''
from operator import attrgetter
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'user({})'.format(self.user_id)

users = [User(23), User(15), User(28)]
print(sorted(users, key=lambda u:u.user_id))

# Alternate approach of using attrgetter instead of lambda.
print(sorted(users, key=attrgetter('user_id')))

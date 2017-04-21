'''
This is simple program to demo how we can short dictonary items based on keys. This also demos itemgetter module
'''

from operator import itemgetter

MyDict = [{"fname": "Michel", "lname":"Scott", "age": 48},
{"fname": "Pam", "lname":"Beasly", "age": 32},
{"fname": "Jim", "lname":"Halpert", "age": 35},
{"fname": "Dwight", "lname":"Shrute", "age": 34},
{"fname": "Kevin", "lname":"Melon", "age": 36},
{"fname": "Bat", "lname":"Man", "age": 00},
{"fname": "Tyrion", "lname":"Lannistor", "age": 31}]

rows_by_fname = sorted(MyDict, key=itemgetter('fname'))
rows_by_age = sorted(MyDict, key=itemgetter('age'))
rows_by_flname = sorted (MyDict, key=itemgetter('fname','lname'))

print(rows_by_fname)
print(rows_by_age)
print(rows_by_flname)

# This also works with the min and max method as shown below
print (min(MyDict, key=itemgetter("age")))
print (max(MyDict, key=itemgetter("age")))

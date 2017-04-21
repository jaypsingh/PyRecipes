record = "0123456789055.210123456789012.78"

#Old Approach
print (record[11:13])
print (record[-5:-1])
totalCost = float(record[10:13]) * float(record[-5:-1])
print (totalCost)

#Suggest Approach
share = slice(11,13)
price = slice(-5, -1)
print (record[share])
print (record[price])
totalCost1 = float(record[share]) * float(record[price])
print (totalCost1)

'''
Suggested Approach is more readable and maintainable.
No body need to wonder in future what all the index is
about in the record.
'''

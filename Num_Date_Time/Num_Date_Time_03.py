'''
Formating output
'''
# Problem : If we add two Decimal numbers a noise is inserted.
myNum = 1234.4321

# Print 2 decimal place
print('MyNum : '+format(myNum, '0.2f'))

# Print right justfied with 2 decimal place.
print('MyNum : '+format(myNum, '>10.2f'))

# Print left justfied with 2 decimal place.
print('MyNum : '+format(myNum, '^10.2f'))

# 1000 seprator
print('MyNum : '+format(myNum, ','))
print('MyNum : '+format(myNum, '0,.2f'))

# Exponential
print('MyNum : '+format(myNum, 'e'))
print('MyNum : '+format(myNum, '0.2E'))

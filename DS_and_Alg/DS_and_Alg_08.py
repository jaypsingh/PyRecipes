#file name : DictZipDemo.zip
'''purpose is to demo how we can invert key and values of a dict in order to
perform some important operation on dictionary using iterator
created by zip module.
Below example shows how we can find min and max in a dictionary'''

priceList = {'iphone':599.00,
'onepluspne':299.00,
'samsungglaxy':199.00,
'googlepixel':399.00,
'Nokia1100':125.00
}

cheapestPhone = min(zip(priceList.values(), priceList.keys()))
print (cheapestPhone)
costlytPhone = max(zip(priceList.values(), priceList.keys()))
print (costlytPhone)

# Short Demo
shortedOrder = sorted(zip(priceList.values(), priceList.keys()))
print (shortedOrder)

'''
Working with Bin, Oct and Hex numbers
'''
# Problem : If we add two Decimal numbers a noise is inserted.
myNum = 1234

# Approach 1
myBinNum = bin(myNum)
myOctNum = oct(myNum)
myHexnum = hex(myNum)
print ("Old Approach ======>")
print('myBinNum : '+myBinNum)
print('myOctNum : '+myOctNum)
print('myHexnum : '+myHexnum)

# Approach 2
print ("New Approach ======>")
print('BinNum : '+format(myNum, 'b'))
print('OctNum : '+format(myNum, 'o'))
print('HexNum : '+format(myNum, 'x'))

'''
Coverting Byte String to integers and vice versa
'''
myData = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(myData))

# from Byte to Int
littleInt = int.from_bytes(myData, 'little')
print (littleInt)
bigInt = int.from_bytes(myData, 'big')
print (bigInt)


# from Int to Byte
print(littleInt.to_bytes(16, 'little'))
print(bigInt.to_bytes(16, 'big'))

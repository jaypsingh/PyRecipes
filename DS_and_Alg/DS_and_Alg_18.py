def countdown(n):
    print("Starting Countdown")
    while n>0:
        yield n
        n = n-1
    print ("Done")
c = countdown(3)
for i in countdown(5):
    print (i)

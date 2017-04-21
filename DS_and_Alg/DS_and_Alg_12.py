'''
This program demos the use of Counter class from collections module.
Counter objects are very helpful in any case where you need to tabulate or count the data.
'''

from collections import Counter
mySong = ['I', 'wanna', 'be', 'your', 't-shirt', 'when', 'it', 'is', 'wet', 'I', 'wanna', 'be', 'the', 'shower', 'when', 'you', 'sweat', 'I', 'got', 'to','be', 'the', 'tattoo', 'on', 'your', 'skin', 'You', 'lemme', 'be', 'your', 'bed', 'baby', 'when', 'you', 'climb']

#More Lyrics
moreLyrics = ['I', 'wanna', 'be', 'your', 'lipstick', 'when', 'you', 'lick', 'it', 'I', 'wanna', 'be', 'your', 'high', 'heels,', 'ah,', 'when', 'you', 'kick', 'it', 'I', 'wanna', 'be', 'sweet', 'love', 'babe,', 'yeah,', 'when', 'you', 'make', 'it', 'From', 'your', 'feet', 'up', 'to', 'your', 'hair,', 'more', 'than', 'anything', 'I', 'swear', 'I', 'wanna', 'be', 'your', 'underwear']

# Create the word count object
wordCount = Counter(mySong)
#under the hood word count is a dictonary
# For example
print (wordCount["wanna"])
print (wordCount["lemme"])

# moset_common() method.
topThree = wordCount.most_common(3)
print (topThree)

'''to update the wordCount variabe we cn do two ways:'''
#Approach 1 <most common which we usually take>
for word in moreLyrics:
    wordCount[word] = +1

# Approach 2 <more efficient which counter object gives us>
wordCount.update(moreLyrics)

'''
#Undocumented freature of counter instance, is that you can do armetical operations like addition or substraction on two counter instances.
eg
wordCount1 + wordCount2
wordCount1 - wordCount2
'''

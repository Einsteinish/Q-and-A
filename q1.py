# Question 1: 

'''
run:
$ python q1.py "Mississippi borders Tennessee."
'''

import sys
import operator

word = sys.argv[1]

# initialize dictionary : all values to 0
mydict = dict.fromkeys(word,0)   

# loop through the input string char by char
# increment the value by 1 if it sees the key 
for c in word:
   mydict[c] += 1

# sort the dict in descening order
sorted_mydict = sorted(mydict.items(), key=operator.itemgetter(1), reverse=True)

# output
for key, value in sorted_mydict:
   print("%s: %s" %(key, '#'*value))


'''
Output

$ python q1.py "Mississippi borders Tennessee."

s: #######
e: #####
i: ####
 : ##
n: ##
p: ##
r: ##
b: #
d: #
M: #
o: #
T: #
.: #
'''
   
   
   





  
   

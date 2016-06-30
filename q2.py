first = ["Mary", "James", "Thomas", "William", "Elizabeth"]
last = ["Li", "O'Day", "Miller", "Garcia", "Davis"]

# construct dictionaly (key, value) = (first, last)
name_dict = dict(zip(first, last))

# sort the dictionary using two keys :
# the key tuple used is (len(last), first)
name_list = sorted(name_dict, key = lambda k: (len(name_dict[k]), k))

# outputs full name
for item in name_list:
  print("%s %s" %(item, name_dict[item]))

'''
outputs

Mary Li
Elizabeth Davis
James O'Day
Thomas Miller
William Garcia
'''

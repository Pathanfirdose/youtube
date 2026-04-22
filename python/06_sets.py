# sets are unordered and unique elements

mysets= {'mon', 'tue', 'wed'}
print(type(mysets))
print(mysets) # it will print in unordered and doesnt print duplicates

mysets.add('thu')
print(mysets)

my_list= ['mon', 'tue', 'wed', 'mon', 'fri']
days_set= set(my_list) # to convert list into set
print(days_set)

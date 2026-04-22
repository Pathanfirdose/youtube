# dictionary is also like list but here we store data in key value pair
 
marks = {'hindi': 57, 'english': 82}
print(type(marks))
print(marks)
print(marks['hindi'])
print(marks['english'])
print(marks.get('telugu')) # if we try to pint print(marks['telugu'] it
# will through error instead we use get syntax returns None if key not found
print(marks.get('hindi')) 
marks['telugu']= 90 # adding item to dictionary
print(marks)

del marks['hindi'] # deleting valus from dictionary
print(marks)

car = {'brand': 'audi', 'model': 'q3'}
print(len(car)) # to get number of key value in dictionary
print(car)
print("my car brand is " + car['brand'])
print('my car model is ' + car['model'])


# strings in python are immutable
f_name = 'firdose'
l_name = 'khan'

fullName = f_name + l_name # concardination
print(fullName)

fullName1 = f_name + ' ' + l_name
print(fullName1)
print(fullName1.upper())
print(fullName1.lower())

message = 'hello world! is my first programm'

print(message.title()) # make it as title - Hello World! Is My First Programm

print(message.split()) # splits text based on space - ['hello', 'world!', 'is', 'my', 'first', 'programm']

print(message.split('!'))  # splits based on '!' - ['hello world', ' is my first programm']

print(message[0]) # it will print only first letter which is 'h'

print(message[0:5]) # it will print range from inex 0 to index 5 which is 'hello'

print(message[-1]) # it will print from reverse which is m

print(message[-1:-8:-1]) # [start:stop:step] it gives in reverse from last

print(message[::-1])




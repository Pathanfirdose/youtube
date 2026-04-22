# create function

# def greetings():
#     print('*'*20)
#     print('welcome user')
#     print('thank you for signing in')
#     print('*'*20)


#calling function
# greetings()
# greetings()
# greetings()

# print('example-1')
# def greetings(user_name, age=None): # if we dont pass any value while calling this function it takes None as a default value
#     print('*'*20)
#     print(f'welcome {user_name}')
#     print(f'age is {age}')
#     print('thank you for signing in')
#     print('*'*20)


# greetings('raju', 20)
# greetings('shyam', 30)
# greetings('ram',) # heere we are not passing value so it will take None

print('example-2')
def greetings(user_name, *hobbies): # if we dont pass any value while calling this function it takes None as a default value
    print('*'*20)
    print(f'welcome {user_name}')
    for hobby in hobbies:
        print(f'hobby is {hobby}')
    print('thank you for signing in')
    print('*'*20)


greetings('raju', 'singing', 'dancing', 'running')
greetings('shyam', 'movies')
greetings('ram', 'reading', 'fighting') # heere we are not passing value so it will take None


print('example-3')
def greetings(user_name, *hobbies): # if we dont pass any value while calling this function it takes None as a default value
    print('*'*20)
    print(f'welcome {user_name}')
    print('hobbies are')
    for hobby in hobbies:
        print(f' - {hobby}')
    print('thank you for signing in')
    print('*'*20)


greetings('raju', 'singing', 'dancing', 'running')
greetings('shyam', 'movies')
greetings('ram', 'reading', 'fighting') # heere we are not passing value so it will take None

print('example-4')
def greetings(user_name, **user_info): # if we dont pass any value while calling this function it takes None as a default value
    print('*'*20)
    print(f'welcome {user_name}')
    for key, value in user_info.items():
        print(f'{key} is {value}')
    print('thank you for signing in')
    print('*'*20)


greetings('raju', age=18, city='delhi', email='xyz@gmail.com')
greetings('shyam', city='delhi', email='xyz@gmail.com')
greetings('ram', city='delhi', email='xyz@gmail.com')

def add(num1, num2):
    return num1 + num2

print(add(10, 30))
result = add(10, 30)
print(result)

if True:
    print('hey its true')
    print('this is if else')
else:
    print('hey its false')

print(10>8)
print(10<8)
print(10==8)
print(10==10)

if 10>8:
    print('hey its true')
    print('this is if else')
else:
    print('hey its false')


# print('enter a number')

# num = int(input('please enter a number - '))

# if num % 2 == 0:
#     print('yes number is even')
# else:
#     print('number is odd') 

# ctrl+/ to comment block

users = ['paul', 'suresh', 'kamal']

if 'khan' in users:
    print('user exist')
else:
    print('user not exist')

users = ['john']

if users:
    print('list is not empty')
else:
    print('list is empty')

# Operators to practice with if else == , >= , <= , != , > , <

marks = int(input('please enter the marks:'))

if marks >=80:
    print('A grade')
elif marks >=60:
    print('B grade')
elif marks >=40:
    print('c grade')
else:
    print('fail')


age = 20
voter_id = False

print('example-1')
if age >=18:
    print('you can vote')
else:
    print('you cannot vote')

print('example-2')
if age >=18:
    if voter_id:
        print('you can vote')
    else:
        print('apply voter id first')
else:
    print('you cannot vote')

print('example-3')

if age >=18 and voter_id: # we can add more 'and' condition
    print('you can vote')
else:
    print('you cannot vote')

print('example-4')

if age >=18 or voter_id:
    print('you can vote')
else:
    print('you cannot vote')



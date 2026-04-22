# While loop

# print('enter a number')


# while True:
#     num = int(input('please enter a number - '))

#     if num % 2 == 0:
#         print('yes number is even')
#     else:
#         print('number is odd')


# user_input = ""
# while user_input != 'q':
#     user_input = input('enter the number or q for quit -')
#     if user_input.isdigit():
#         if int(user_input) % 2 == 0:
#             print('yes number is even')
#         else:
#             print('number is odd')


print('example-1')
num = [10, 20, 30, -50, 20, -30]

for n in num:
    if n == 30:
        break
    print(n)

print('example-2')
num = [10, 20, 30, -50, 20, -30]

for n in num:
    if n == 30:
        continue
    print(n)

print('example-3')
num = [10, 20, 30, -50, 20, -30]

for n in num:
    if n == 30:
        continue
    print(n)
    print('step1')

print('example-4')
num = [10, 20, 30, -50, 20, -30]

for n in num:
    if n > 0:
        continue
    print(n)

print('example-5')
num = [10, 20, 30, -50, 20, -30]

for n in num:
    if n < 0:
        continue
    print(n)
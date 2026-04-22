print(10*2)

try:
    print(10/0)
except ZeroDivisionError:
    print('kindly do not divide by zero')

print(10+2)
print(10-2)

try:
    with open('user_info1.txt', 'r') as file:
        content = file.readlines()
except FileNotFoundError:
    print('file not found')
else:
    for line in content:
        print(f'welcome {line.rstrip()}')


try:
    with open('user_info.txt', 'r') as file:
        content = file.readlines()
except Exception as e:
    print(e, type(e))
else:
    for line in content:
        print(f'welcome {line.rstrip()}')
finally:
    print('DB Closed')
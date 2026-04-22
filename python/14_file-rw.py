# with open('user_info.txt', 'a') as file:
#     file.write('this is my first file in python\n')

with open('user_info.txt', 'r') as file:
    content = file.readlines()

for line in content:
    print(f'welcome {line.rstrip()}')
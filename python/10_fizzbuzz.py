print('fiz buzz program')

till_num = int(input('enter the number - '))

my_list = []

# for num in range(1, till_num+1):
#     my_list.append(num)
# print(my_list)

for num in range(1, till_num+1):
    result = ""
    if num % 3 == 0:
        result = result + 'fizz'
        if num % 5 == 0:
            result = result + 'buzz'
    elif num % 5 == 0:
        result = result + 'buzz'
    else:
        result = num
    my_list.append(result)
print(my_list)
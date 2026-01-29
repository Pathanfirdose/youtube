user_list = ['firdose', 'moin', 'aisha', 'nizam'] # list of names

print(user_list) # it prints user list

user_list[0]="Firdose" # if you want to make change to list

print(user_list[0]) # it prints first name in list

print(user_list[1]) # it prints second name in list

user_list.append('mohsin') # it adds name to list

print(user_list)

user_list.remove('moin') # it removes name from list

print(user_list)

user_list[1] = 'Moin'

print(user_list)

user_list.insert(1, 'moin') # to add name in specific index
print(user_list)

del user_list[4] # it deletes from specific index
print(user_list)

print('length starts')

#no of items in list
print(len(user_list))

# sorting list from a to z
user_list.sort()
print(user_list)

# sorting list form z to a
user_list.sort(reverse=True)
print(user_list)

# reverse the list without sort
user_list.reverse()
print(user_list)

user_list1 = ['firdose', 'moin', 'aisha', 'nizam']
user_list1.pop() # removes last item
user_list1.pop(0) # removes first item
# diffarence between pop and remove is pop gives it as output and we can store pop in variable

removed_value = user_list1.pop()
removed_value1 = user_list1.pop(0)


print(user_list1)
print(removed_value)
print(removed_value1)

# Slicing of list
user_list2 = ['firdose', 'moin', 'aisha', 'nizam', 'mohsin', 'sara']

print(2)
print(user_list2[1:4]) # from index 1 to 3
print(user_list2[:3]) # from start to index 2
print(user_list2[-2:]) # from index 2 to end

# Numeric list
marks = [57, 82, 79, 71, 77, 64]
print(marks)
print(min(marks))
print(max(marks))
print(sum(marks))
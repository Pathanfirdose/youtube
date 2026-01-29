user_list = ['firdose', 'moin', 'aisha', 'nizam']

print(user_list)

print(user_list[0])

print(user_list[1])

user_list.append('mohsin')

print(user_list)

user_list.remove('moin')

print(user_list)

user_list[1] = 'Moin'

print(user_list)

user_list.insert(1, 'moin')
print(user_list)

del user_list[4]
print(user_list)

#no of items in list
print(len(user_list))

# sorting list
user_list.sort()
print(user_list)

# sorting list
user_list.sort(reverse=True)
print(user_list)

# reverse the list
user_list.reverse()
print(user_list)

user_list1 = ['firdose', 'moin', 'aisha', 'nizam']
user_list1.pop() # removes last item
user_list1.pop(0) # removes first item
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
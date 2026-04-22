# tuples are immutable means we cannot change and ordered

days = ('mon', 'tue', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
# though we cannot modify tuple but we can add another tuple
#days = ( 10, 20)
print(type(days))
print(days)
print(days[0])
print(days.count('tue')) # it prints how many times 'tue' has come
print(days)
print(days.index('fri')) # it prints the index of tuple
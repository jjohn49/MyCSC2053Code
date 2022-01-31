coordinates = (5,25)
print(coordinates)

#initialize multiple variables using a tuple
x , y = coordinates
print(x,y)

'''coordinates[0] = 1 
if u uncomment this u get an error b/c
you cannot change values in a tuple'''

set1 = {1,2,3,3,4,5}
#sets will remove all duplicates
#only prints {1,2,3,4,5}
print(set1)

list1 = [1,2,2,3,4,5]
list_remove_doubles = set(list1)
print(list_remove_doubles)

'''set1[4] = 7
sets are not stored like lists in order so u cannot change a value at a certain index'''

list2 = []
for i in range(0,50):
    list2.append(i)
print(list2)

#list3 is identical to list2 but took a lot less code
list3 = [x for x in range(0,50)]
print(list3)

#add conditionals afterwards to make it better
list4 = [x for x in range(0,50) if x > 40]
print(list4)

evens = [x for x in range(0,50) if x % 2 == 0]
print(evens)

odds = [x for x in range(0,50) if x % 2 == 1]
print(odds)



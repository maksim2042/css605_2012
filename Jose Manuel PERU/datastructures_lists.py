#!/CSS 605 - Object OSS/github/css605_2012/Jose Manuel PERU
# Filename: datastructures_lists.py
#PRACTICING some functionality of Lists in Python!!

import random  #I will need this later for a random selection
def listItems(list):
	for item in list:  #sequence!!
		print '-',item

		
supplyList = ['Book on Python', 'Memory stick', 'Pencils', 'Chewing Gum'] # My supply list

print 'I have', len(supplyList), 'items to purchase.'# My list count 
print 'These are the items needed:' # My list printed

listItems(supplyList)

print '\nI also have to buy a new mobile!!!.'
newItem='Mobile'
supplyList.append(newItem) #adding a new item

print '\nAnd an ipad and a new backpack '
newList=['Ipad','Backpack']
supplyList.extend(newList) #adding a new list


supplyList.sort() #sorting the list (mutability!!!!)
print 'This is an alphabetical version of my list'
listItems(supplyList)

#At the store:
randomChoice=random.randint(0, len(supplyList)-1) #getting a integer random index 
print 'What should I buy first???', supplyList[randomChoice], 'Right!'

olditem = supplyList[randomChoice] #deleting the item and seeing the new list!!!!
del supplyList[randomChoice]
print 'After buying', olditem,'I just need'
listItems(supplyList)
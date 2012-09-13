'''
Created on Sep 13, 2012
PRACTICING some functionality of Tuples in Python!!
@author: josemagallanes
'''
#!/CSS 605 - Object OSS/github/css605_2012/Jose Manuel PERU
# Filename: ds_tuples.py

import myfunctions

supplyList = ['Book on Python', 'Memory stick', 'Pencils', 'Chewing Gum', 'Mobile','Ipad','Backpack'] # My supply list
print "List:",supplyList

tupleSupplies = tuple (supplyList)
print "Tuple:",tupleSupplies 

tupleord=supplyList
tupleord.sort()
tupleSuppliesOrd=tuple(tupleord)
print "Same tuple (ordered)",tupleSuppliesOrd 
tupleSuppliesOrd1=tupleSuppliesOrd
tupleSuppliesOrd2=tupleSuppliesOrd + ('zipdrive',) 

print cmp(tupleSupplies, tupleSuppliesOrd) 
# Its 1, since 'Book...' (first element in tupleSupplies) is greater than 'Backpack...'  
print cmp(tupleSuppliesOrd, tupleSupplies)
# Its -1, since 'Backpack...' (first element in tupleSuppliesOrd) is less than 'Book...'  
print cmp(tupleSuppliesOrd, tupleSuppliesOrd2)
# Its -1, since tupleSuppliesOrd has one element less than tupleSuppliesOrd2 
print cmp(tupleSuppliesOrd1, tupleSuppliesOrd)
# Its 0, they are identical


tupleSuppliesOrd3=myfunctions.del_tupelem(tupleSuppliesOrd2,'zipdrive')
print cmp(tupleSuppliesOrd1, tupleSuppliesOrd3)
'''
Created on Sep 13, 2012
Practicing Making Modules
@author: josemagallanes
'''

def listItems(lista):
    for item in lista:  #sequence!!
        print '-',item
        
def del_tupelem(tup, tupelem):
    pos=0
    while tup[pos]!=tupelem:
        pos+=1
    part1=tup[0:pos]
    part2=tup[pos+1:]
    return part1 + part2
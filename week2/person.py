"""
This is a long long long comment 
that describes person.py file
"""

class Person():
	def __init__(self, name, sex, age=0, height=0):
		self._name_=name
		self.__sex__=sex
		self.age=age
		self.height=height
	
	def walk(self):
		print self._name_," is now walking"
		
		
class Baby(Person):
	
	def walk(self):
		print self._name_," hasn't learned to walk yet"
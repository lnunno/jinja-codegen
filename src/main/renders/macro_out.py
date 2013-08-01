
class Person(object):
	'''Classdocs
	'''
	
	def __init__(self,age,name):
		'''docs
		'''
		self.age = age		
		self.name = name		
		



class Doctor(Person):
	'''Classdocs
	'''
	
	def __init__(self,age=30,name="John",med_school="BYU"):
		'''docs
		'''
		super(Doctor,self).__init__(age=30,name="John") 
		self.age = age		
		self.name = name		
		self.med_school = med_school		
		



def say_hello(greeting="Hello",name="You" ):
		pass

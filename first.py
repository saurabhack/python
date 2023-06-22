class first(object):
    
	def info_students(self):
		self.name=str(input("enter your name="))
		self.age=int(input("enter your age="))
		self.tatal=int(input("enter your total marks="))

		print(self.name)
		print(self.age)
		print(self.tatal)

	
class second(first):

	def parent_info(self):
		self.name=str(input("enter your parents name name="))
		self.age=int(input("enter your parents age"))
		self.worker=str(input("enter your job profile , profession , etc="))

		print(self.name)
		print(self.age)
		print(self.worker)


class third(second,first):
	def memorize(self):
		self.record=str(input("enter the record of students which is clear or not="))
		print(self.record)

	


obj3=third()

obj3.info_students()
obj3.parent_info()
obj3.memorize()

	
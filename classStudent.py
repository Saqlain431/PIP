class student:
	def __init__(self):
		self.age=None
		self.id=None
		self.marks=None
		self.name=None


	def set(self):	
		print("Enter name, id ,age and marks\n")
		self.name=input("Enter name\n")
		self.age=int(input("Enter age\n"))
		self.id=input("ENter usn\n")
		self.marks=int(input("ENter marks\n"))


	def get(self):
		print("name:"+self.name+"\n")
		print("id:"+self.id+"\n")
		print("age:"+str(self.age)+"\n")	
		print("marks:"+str(self.marks)+"\n")

	def validate_marks(self):
		if(self.marks>=0 and self.marks<=100):
			return True
		return False

	def validate_age(self):
		if(self.age>20):
			return True
		return False

	def check_qual(self):
		if self.validate_age() and self.validate_marks():
			if self.marks>=65:
				return True
		return False

ob=student()
ob.set()
if ob.check_qual():
	print("\n valid student\n")
	ob.get()
else:
	print("invalid student\n")

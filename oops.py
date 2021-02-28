class  Visitors:
	present_age = 2021
	def __init__(self, name, birth_age):
		self.name = name
		self.birth_age = birth_age
	def print_with_hello(self):
		return "Hello " +  self.name
	def calculate_age(self):
		return f"Your age: { Visitors.present_age - self.birth_age }"
user_name = input('Enter your name: ')
user1 = Visitors(user_name, 1999)
print(user1.print_with_hello())
print(user1.calculate_age())

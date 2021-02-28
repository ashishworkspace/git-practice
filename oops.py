class  Visitors:
	present_year = 2021
	def __init__(self, name, birth_year):
		self.name = name
		self.birth_year = birth_year
	def print_with_hello(self):
		return "Hello " +  self.name
	def calculate_age(self):
		return f"Your age: { Visitors.present_year - self.birth_year }"

user_name = input('Enter your name: ')
user1 = Visitors(user_name, 1999)
print(user1.print_with_hello())
print(user1.calculate_age())

input_salary = input('Enter the Salary: ')
class Employee(Visitors):
	def __init__(self, name, salary, birth_year=None):
		super().__init__(name, birth_year)     # I don't want birth_year variable
		self.salary = salary
	def print_employee_salary(self):
		return  f"{self.name} your salary is {self.salary}"
user2 = Employee(user_name, input_salary)
print(user2.print_employee_salary())
# end of the program
####################

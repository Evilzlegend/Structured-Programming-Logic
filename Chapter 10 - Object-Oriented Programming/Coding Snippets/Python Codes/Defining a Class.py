# Topic Summary:
# You can create your own kind of objects by creating a class. In the class you can list methods and
# define variables that belong to objects of the class. A class declaration starts with the word class
# followed by the name of the class. If it has a parent class, that is put in parentheses after the name.
# Then all methods (and class variables) are indented:

# Coding Example:

# class <className>(<parentClass>):
#	<statements>

# The statements inside the class declaration are usually method definitions look like
# regular function definitions, except that the first input is the special variable self, which is a reference
# to the object itself. When calling the method, no value for self is passed.

# Playing with Coding Snippets:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

class Rodent:

	def bite(self, num=1):
		for i in range(num):
			print("Bite!")

	def chew(self, num=1):
		for i in range(num):
			print("Chew!")

	def getName(self):
		return "Rodent"

rat = Rodent()
rat.bite(3)
rat.chew()
print(rat.getName())
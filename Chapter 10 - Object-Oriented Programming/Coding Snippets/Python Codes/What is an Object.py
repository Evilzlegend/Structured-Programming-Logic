# Topic Summary:

# An object is a collection of data that also has associated methods that allow us to ask the object about
# its data, and even to modify its data, in some cases. Objects each have a specific type, and the methods
# associated depend on the type of the data.

# Coding Example:

# To call an object's method, we first list the name of the object, then a period, then the method's name,
# and finally parentheses with any inputs in it. This syntax is similar to calling a function in a module.

# <object>.MmethodName>(<inp1>, <inp2>, ...)

# Lists, strings, and dictionaries are all common built-in object, but most built-in datatypes in Python are
# implemented as objects, and many of them have methods. Iteratos are produced by the 'range'
# function or dictionary access methods.

# Playing with Coding Snippets:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

lst = ['raspberry', 'pear', 'apple']
print(lst)
lst.sort()
print(lst)
lst.insert(2, 'guava')
print(lst)
myStr = "I love fruit!"
print(myStr.upper(), myStr.title())
print(myStr.replace('fruit', 'vegetables'))
d = {'abby': [3, 4, 1], 'raga': [6, 2, 5]}
print(d.get('raga'), d.get('paulo'))
r = range(2, 25, 3)
print(r)
x = 3
y = 4.5
z = 25123
print("numeric methods:", x.bit_length(), y.is_integer(), z.bit_length())

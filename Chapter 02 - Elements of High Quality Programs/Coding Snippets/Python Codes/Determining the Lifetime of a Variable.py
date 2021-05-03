# TOPIC SUMMARY:
# The lifetime or extent of a variable indicates the periods of time during the running of a program when
# the variable is "live" and in use. Global variables have an unlimited lifetime. Once created, they remain
# active and available for use throughout the remainder of the program.

# TOPIC EXPLANATION:
# Parameters and local variables, however, have a limited lifetime. They come into being when their
# function is called, and remain active during the function call. When the call ends, they come to an end
# as well. Before and after the call, parameter and local variables do not exist.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

x = 55

def adder(z):
    print(z, "is live during this call to adder")
    return z + 3

print(x, "is always available")
print("Calling adder...")
print(adder(12))
print(x, "is still available")
# print(z, "is not available now") # an error if run
# Topic Summary:
# Local variables are only visible inside the function where they are created.
# In some ways a function definition is just a fancy way to creating a
# variable, bound to a function object. It follows, perhaps, that we can
# define local functions just like we can create local variables.

# Topic Explanation:
# A local funtion is defined indented inside another function. It may be
# called from inside the outer function, but not from anywhere else. This
# can be useful for a helper function that no other part of the program ever
# needs to access. The local function doesn't clutter up the global variable
# namespace.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

def multCallPolynomial(startVal, endVal):
    """Calls a built-in polynomial for every value between startVal
    and endVal, printing the results."""
    def poly(x):
        """Takes in x and computes 3x^2 + 2x + 1, returning the
value."""
        return 3 * x ** 2 + 2 * x + 1
    for v in range(startVal, endVal+1):
        print(v, poly(v))

multCallPolynomial(0, 20)
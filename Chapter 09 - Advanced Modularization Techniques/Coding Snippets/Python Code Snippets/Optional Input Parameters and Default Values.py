# Topic Summary:
# Some functions have optional inputs, where a function call need not provide a
# value for every input. A function definition may specify that some of its
# parameters are optional by giving a default value to be used if a function call
# omits them. If no default value is specified, then the input is required.

# Topic Explanation:
# The syntax for an optional parameter looks like an assignment statement inside
# the list of parameters in the function definition line. All required parameters
# must come before any optional parameters.

# The function call must first give values for each required input. It may stop after
# the required inputs, or it may give optional values in the order they appear. See
# "Passing Values by Parameter Name" for another way to select or reorder input
# parameters.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

def buildSentence(noun, verb, witha="", ona="", fora=""):
    baseString = noun + " " + verb
    if witha !="":
        baseString += " " + witha
    if ona != "":
        baseString += " " + ona
    if fora != "":
        baseString += " " + fora
    return baseString

s1 = buildSentence("Marguerite", "sings")
print(s1)
s2 = buildSentence("Randall", "jumps", "with a rope", "on a car")
print(s2)
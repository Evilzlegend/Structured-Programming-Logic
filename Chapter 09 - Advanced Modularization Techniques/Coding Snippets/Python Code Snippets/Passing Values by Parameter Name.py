# Topic Summary:

# A function call may specify both required and optional inputs by the parameter
# name. This looks like an assignment statement inside the parentheses of the
# function call. The parameter names must match exactly with those used in the
# call.

# Topic Explanation:

# This method of assigning values to input parameters may be used to specify
# inputs in any order the programmer chooses, or to select only some optional
# inputs.

# PLAYING WITH CODING SNIPPETS:
# 1. Hit the Run button to see the output in the snippet box.
# 2. Play around with the snippet code - change variable names, parameters, etc.
# 3. Hit the Run button again to see what works and what does not work after you manipulate the code.
# 4. Run the correct code again to compare it to the manipulated code.
# 5. Have fun practicing this snippet as many times as you like - there are no limits!

def buildSentence(noun, verb, witha="", ona="", fora=""):
    baseString = noun + " " + verb
    if witha != "":
        baseString += " " + witha
    if ona != "":
        baseString += " " + ona
    if fora != "":
        baseString += " " + fora
    return baseString

s3 = buildSentence("Sarah", "waits", fora="friend")
print(s3)
s4 = buildSentence(ona="tabletop", verb="dances", noun="Brett")
print(s4)
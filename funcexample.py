#The following is an example of a function being defined, and then called later in the program

def myfunction():
    print ("Hello World!")

myfunction()

#Define, Call, Pass, Argument, Parameter - Definitions:

#To define a function is to create it , just like an assignment like spam = 42 creates the spam variable. Calling a function refers to the previous example, where I used the myfunction() line to call the previously defined myfunction()

#When we refer to a pass, we're taking something and sending it into the function for use within the function. For example:

def yourfunction(somevariable):
    myparam = somevariable
    print (myparam)

definedvariable = ("Goodbye World!")
yourfunction(definedvariable)

#What we've done here is 1. defined yourfunction(), 2. called yourfunction(), 3. passed the variable definedvariable. 4. This value being passed to a function is an argument; if the argument is assigned to a local variable within the function, this is known as a parameter 

#------------------------------------------------------------------------

#We also have the ability to return values in a function, so that they can be used elsewhere in the program. For example:

def somefunction():
    answer = 5 + 5
    return answer

print (somefunction())

#Here we 1. defined a function (somefunction) that returns the 'answer' variable to where the function was called, and 3. we print the returned value after the function is called. 

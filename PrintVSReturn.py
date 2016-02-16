#This file is meant to serve as an introduction to Python syntax and basic commands.
#It should be completed in linear order.
#Don't be afraid to "try it and see what happens". That's what version control
#is for. There is a working copy saved somewhere.
#Questions are awesome. Curiousity helps you learn.


#defining a function
#A "function" is what Python uses to perform operations. This is a function:
def helloWorld():
    print "hello, world!"

#This function has a declaration, and one task.
#Its name is "helloWorld"
#It has no parameters
#It prints a string, but it doesn't return anything.

#defining a function with parameters
def helloWorld(name):
    print "hello, world! My name is" + name

#This function takes in a parameter.
#It takes in parameter 'name'.
#It performs an operation on the parameter.
#Everytime the function is called, the parameter can be changed.

#What do you expect to happen when this file is run?


#Ans: nothing will happen, because none of the methods are being called.
#The syntax for calling a method is:
#helloWorld()

#Remove the '#' from line 32 and run the file again. What happens?

#Ans: "hello, world!" is printed to the console
#See if you can run helloWorld(name).

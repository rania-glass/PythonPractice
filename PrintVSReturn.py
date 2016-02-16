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
# parameter name is a string, and must be entered using quotes.
def helloWorld(name):
    print "hello, world! My name is" + name

#This function takes in a parameter.
#It takes in parameter 'name'.
#It performs an operation on the parameter.
#Everytime the function is called, the parameter can be changed.
#This function still doesn't return anything.

#What do you expect to happen when this file is run?


#Ans: nothing will happen, because none of the methods are being called.
#The syntax for calling a method is:
#helloWorld()

#Remove the '#' from line 34 and run the file again. What happens?

#Ans: "hello, world!" is printed to the console
#See if you can run helloWorld(name). You can do this by changing one line.
#Can you call "helloWorld("name")" using your name as a parameter, so that it prints
#"hello, world! My name is [yourname]"?

#Return functions
def returnWorld():
    return "return the world!"

#What happens when you run the function above?
#returnWorld()
#What happens when you print the result of the function above?
#print returnWorld()

#What is the difference between print and return?
#See additional practice file for some pre-defined functions that
#demonstrate the difference between printing and returning.




#How can you use print statements effectively to check what's being returned?
#What happens if you don't return anything, but do print something?
#What happens if you don't print anything, but do return something?

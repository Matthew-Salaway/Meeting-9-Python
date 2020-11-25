# Copy this code into your own repl. Click the navigation bar in the top left corner and go to My Repl.
# Click the New Repl on the left, create the repl, and paste the code. Or put into another IDE.

# Today will be part 2 of the Python review in preparation of the coding competition

# The competition will be on Wednesday, December 9
# 3 challenges, groups of 3 or 4, 30 minutes
# Winners each get $10 gift cards

# Now for the review

# Let's review functions

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function. A function can return data as a result.
# Functions are useful for code that needs to be repeated

# First we will create a simple function. Create a function called sayHello (use def) and make it
# print "Hello Scottsdale Arizona"
def sayHello():
    print("Hello Scottsdale Arizona")
sayHello()


# Now we will make a function with parameters. Create the function customizedHello with the parameters:
# name and age. Then make the program print "Hello [name]. You are age: [age]"
def customizedHello(name, age):
    print("Hello " + name + ". You are age: " + str(age))
customizedHello("Matthew", 18)

# The next function will be called graduate. In order to graduate from Chaparral High School
# the student needs to pass course requirements and the civics test. There are 2 parameters to the
# function and both of them are booleans. The first parameter is "curriculum" and the other is "civics"
# If both are true, print "You graduated!"
# Any are false, print out "You still need to complete " followed by the missing requirements

def graduate(curriculum, civics):
    if curriculum and civics:
        print("You graduated!")
    elif curriculum and not civics:
        print("You still need to pass the Civics Test")
    elif not curriculum and civics:
        print("You still need to complete the required courses")
    else:
        print("You still need to pass the Civics Test and complete the required courses")

graduate(True, True)
graduate(False, True)
graduate(True, False)
graduate(False, False)

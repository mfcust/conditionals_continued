#1) Create a variable called food that stores user input for the question "Do you like pizza?" Then use a conditional IF and ELSE statement to print a different response
#if you answer yes or no. (HINT: You will need to use the input() function in your variable declaration statement)





# 2a) Ask the user "What's your favorite number?" and store that as a variable called number. The response you type in will be a string that you will have to convert into
# either a float or int. You can do this in your variable declaration statement by using the float() or int() function wrapped around your value. For example, if I had
#a variable x that was equal to the string value '5', then in order to change the string value '5' to a float, I could convert it by saying x = float('5'). For this
question, you need to have everything inside your float() or int() function, including your input() function (e.g. x = float(input("Question")))



# 2b) Now write a program that uses 1 IF statement, 2 ELIF statements, and 1 ELSE statement that prints something different depending on the user input number. Here is the
#logic for your program: if the number is less than zero, print "That's a negative number!" else if the number is exactly equal to zero, print "Your favorite number has no value!"
#else if the number is less than or equal to 99 print "Your favorite number is only one or two digits!" else print "That's a big number!" Test your program by inputting
#different numbers that satisfy each condition!!!








# 3) You can also put if, elif and else statements inside of each other by using the correct indentation. Uncomment the block of code below to observe:
'''
x = 100

if x >50:
  if x == 100:
    print("I like the number 100")
    
  elif x==200:
    print("200 is twice as good as 100")
    
  else:
    print("All these numbers are ok I guess."
    
else:
  print("These numbers are too small")
'''

#Run the program when x = 100, when x = 200, when x = 1000, and when x = 10. Write what happens for each value of x below by using comments:








# 4)Nested conditional statements are when you have if, elif and else statements inside of other if, elif and else statements. Create a program similar to the one in
#question 3 where you first ask the user "Do you have a favorite food?". If they answer yes, then ask the question "What is your favorite food?" and nest an if, 2 elifs and an else
inside with different print functions depending on the answer to the second question. If they answer no, then print something in your original else statement.












#--------------------------------------------------------------------------------------------------------------------------#
#Bonus Questions

#1) You can use conditional statements to direct your turtle to do different commands as well. Set up your turtle by importing the library and creating variable t
#equal to the turtle pen. Then, use a conditional if, elif and else statement that has your turtle do something cool depending on what color you choose for the pencolor.
#I recommend having your turtle draw a different shape for each color, though you can make the program as complex as you want it. (HINT: You may need to use an input()
#function to get a color from the user, and then use that variable in your .pencolor() method, as well as use the color in your if and elif conditions.












#2) Your nested conditional statements don't need to stop at just one layer of nesting! Write a program that has at least 3 layers of nesting with conditional statements.
#How many layers deep can you go??? I recommend asking the user a series of questions and printing a response for each combination of answers. I look forward to seeing what you come up with!
















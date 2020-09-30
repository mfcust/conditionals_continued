# else statements

Consider the following conditional statement and code:
```
color = input("What is your favorite color? ")

if color == "green":
  print("My favorite color is green too! It reminds me of FROGS!")
```
color == "green" is a boolean expression that asks "Is the variable color exactly equal to green?" Because we have an IF statement here, the code with the print function only runs if this boolean expression is True. But what if I wanted something else to print if color == "green" was False? Here I can use an Else statement, which means "In all other cases."

In English this sounds like this: If the user's favorite color is green, then say "My favorite color is green too! It reminds me of FROGS!", or else in all other cases say something else. Let's see how this looks in Python code:
```
color = input("What is your favorite color? ")

if color == "green":
  print("My favorite color is green too! It reminds me of FROGS!")
  
else:
  print("That's cool! But I like Green more!")
```

In this scenario, Python looks at the first IF statement to decide if the boolean expression is True or not. If it's True, then it doesn't even look at the else statement. However, if it's False, Python skips over the IF statement and runs the Else statement instead.

# elif statements
Lastly, we have elif statements, which stand for "else-if." These are useful if you would like to specify multiple specific conditions. Notice how the else statement above has no boolean expression. Elif statements do, and you can have as many of them as you want. For example:
```
color = input("What is your favorite color? ")

if color == "green":
  print("My favorite color is green too! It reminds me of FROGS!")

elif color == "blue:
  print("Do you like the beach?")

elif color =="red":
  print("Red is nice!")
  
else:
  print("That's cool! But I like Green more!")
  
As you can see, you can have multiple elif statements that specify othe rconditions. They all depend on the other, so if one is False then Python moves to the next one. If one is True, then Python doesn't bother looking at the rest.

Navigate into the Python file to practice using if, elif and else statements!
```

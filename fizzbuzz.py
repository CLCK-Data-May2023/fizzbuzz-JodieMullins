"""
Challenge: Write a Python program that prints the numbers from 1 to 100. 
If the number is dividable by 3 print Fizz, if the number is dividable by 5 print Buzz 
instead of the number. If the number is dividable by 3 and 5 print FizzBuzz.

**Comments are excess code but relevant documentation
"""

for number in range(1, 101): # prepares a loop to work with 
                             # an iterating variable (named number) and numbers from 1 - 100 

    
    if number % 3 == 0 and number % 5 == 0: # Asks if number is divisible by 3 AND 5, such as 15
    #    number = "FizzBuzz"
        print("FizzBuzz")
    #    continue 
    
    elif number % 3 == 0: # If number is not divisible by 3 AND 5, is it divisible by 3?
    #    number = "Fizz"
        print("Fizz")
    #    continue
    
    
    elif number % 5 == 0: # If number is not divisible by 3 AND 5 or only 3, is it divisible by 5?
    #    number = "Buzz"
        print("Buzz")
    #    continue
        
    
    else: # All checks have failed; number is not divisble by any conditions provided
    #    number = number 
        print(number)# add your code here


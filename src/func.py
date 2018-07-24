# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard
num = input("Enter a number: ")

def is_even(num):
    if num % 2 == 0:
        return True
    else: 
        return False



if is_even(int(num)): 
    print("Even!")
else: 
    print("Odd")

# Print out "Even!" if the number is even. Otherwise print "Odd"
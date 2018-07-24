# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []
i = 0 
while i != 5:
    i += 1
    y.append(i) 
print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = []
i = 0 
while i != 9:
    i += 1
    y.append(i**3) 
print (y)



# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

def upper(x): return x.upper()
y = list(map(upper, a))
print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = []

print(y)



nums = [0,1,2]
for index, num in enumerate(nums):
  print(num, index)
x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
print('y is %f, and z is %s' %(y,z)); 
# x is 10, y is 2.25, z is "I like turtles!"
print('x is %d, y is %f, z is %s' %(x,y,z)); 

# Use the 'format' string method to print the same thing
print('x is {}, y is {}, z is {}'.format(x, y, z))




# ```x = 10
# y = 2.24552
# z = "I like turtles!"

# # Using the printf operator (%), print the following feeding in the values of x,
# # y, and z:
# # x is 10, y is 2.25, z is "I like turtles!"
# print("x is %d, y is %.2f, z is \"%s\"" % (x, y, z))

# # Use the 'format' string method to print the same thing
# print("x is {}, y is {:.2f}, z is \"{}\"".format(x, y, z))```


# Moises Dobarganes [1:00 PM]
# i like string litterals with ' '.format() way better

# Aaron [1:00 PM]
# print('x is %d, y is %1.2f, z is "%s"' % (x, y, z))

# print('x is {0}, y is {1:1.2f}, z is "{2}"'.format(x, y, z))

# Justin [1:00 PM]
# ```print("x is %d, y is %f, z is %s" % (x, y, z))

# # Use the 'format' string method to print the same thing
# print(("x is {0}, y is {1}, z is {2}").format(x, y, z)) # access arguments by position
# print(("x is {x}, y is {y}, z is {z}").format(x = 10, y = 2.24552, z = 'I like turtles!'))``` 
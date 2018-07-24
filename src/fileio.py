# Use open to open file "foo.txt" for reading
file = open("foo.txt", "r") 
file_object = file.read()
# Print all the lines in the file
print(file_object) 

# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file2 = open("bar.txt", "w") 
# Use the write() method to write three lines to the file
file2.write("imran imran")
file2.close()

afterWrite =open("bar.txt", "r")
file_object2 = afterWrite.read()
print(file_object2)

# Close the file

afterWrite.close()
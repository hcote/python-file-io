# Youtube tutorial
# https://www.youtube.com/watch?v=Uh2ebFW8OYM

# if file is in different directory, need to pass the path through
# r = read-only, w = write-only, a = append, r+ = read+write
f = open("test.sh", "r")
f = open("test.sh", "w")
f = open("test.sh", "a")
f = open("test.sh", "r+")
print(f.name) # self-explanitory
print(f.mode) # prints 'r' if you opened it just for reading
# need to close a file after using it - otherwise you can end up with leaks and apps may throw an error
f.close()

# ***** Reading Files:

# disregard above - here we're creating f a better way
# this also automatically closes the file after running
with open("test.sh", "r") as f:
	pass

	# For small Files:
	f_contents = f.read()
	print(f_contents) # prints entire file (loads it into memory)

	# For big Files:
	f_contents = f.readlines()
	print(f_contents) # prints all lines in a file in a list (each line is an element)
	# if you do the following, only prints the first line:
	f_contents = f.readline()
	# and if you write it again, it will read the next line, and so forth

    # With the extra lines:
	f_contents = f.readline()
	print(f_contents)
	f_contents = f.readline()
	print(f_contents)

	# Without the extra lines:
	f_contents = f.readline()
	print(f_contents, end = '')
	f_contents = f.readline()
	print(f_contents, end = '')

	# Iterating through each line in the file:
	# Doing it this way isn't a memory issue bc it does them one by one and not all at once
	for line in f:
		print(line, end = '')

	# Going Back....:
	f_contents = f.read()
	print(f_contents, end = '')

	# Printing by characters:
	f_contents = f.read(100)
	print(f_contents, end = '')
	# picks up where it left off, so will return the next 100 characters
	f_contents = f.read(100)
	print(f_contents, end = '')
	f_contents = f.read(100)
	print(f_contents, end = '')

	# Iterating through small chunks:
	# It will break out of the while loop once there's nothing left to read
	size_to_read = 100
	f_contents = f.read(size_to_read)
	while len(f_contents) > 0:
		print(f_contents)
		f_contents = f.read(size_to_read)

	# Iterating through small chunks, with 10 characters:
	size_to_read = 10
	f_contents = f.read(size_to_read)
	print(f_contents, end = '')
	f.seek(0)
	f_contents = f.read(size_to_read)
	print(f_contents, end = '')
	print(f.tell()) # returns the character number in the file we're at
	while len(f_contents) > 0:
		print(f_contents, end = '*')
		f_contents = f.read(size_to_read)
print(f.mode)
print(f.closed) # returns True
print(f.read()) # throws error


# ****** Writing Files:

# The Error:
with open("test.sh", "r") as f:
	f.write("Test")
	# error because you're writing to a read-only file

# Writing Starts:
with open("test2.txt", "w") as f:
	pass # just these two lines (94 & 95) will create a new file
	f.write("Test")
	f.seek(0) # sets new position to start writing at the 0th char (it will overwrite if there's already characters there!)
	f.write("Test")
	f.seek("R") # changes the first char: goes from "Test" to "Rest"

# Copying Files:
# opening one (the original file) in read-only
with open("test.sh", "r") as rf:
	# creating another (the copy) file in write-only
	with open("test_copy.sh", "w") as wf:
		# for each line in the read-only file
		for line in rf:
			# write it to the write-only file
			wf.write(line)

# Copying the/your image:
# Same code as above throws an Error (because you need to decode it in binary first)
with open("bronx.jpg", "r") as rf:
	with open("bronx_copy.jpg", "w") as wf:
		for line in rf:
			wf.write(line)
			

# Copying the image starts, without chunks:
# changing r => rb & w => wb you can copy images
with open("bronx.jpg", "rb") as rf:
	with open("bronx_copy.jpg", "wb") as wf:
		for line in rf:
			wf.write(line)

# Copying the image with chunks:
with open("bronx.jpg", "rb") as rf:
	with open("bronx_copy.jpg", "wb") as wf:
		chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

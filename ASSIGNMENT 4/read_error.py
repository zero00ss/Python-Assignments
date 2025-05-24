try:
	file1 = open(r"c:\Users\hp\Documents\Python Assignments\ASSIGNMENT 4\sample.txt", "r")
	read_file= file1.read()
	print(read_file)
except FileNotFoundError: 
	print("File not found")

file1.close()


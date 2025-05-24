try:
	file1= open("sample.txt", "r")
	read_file= file1.read()
	print(read_file)
except FileNotFoundError: 
	print("File not found")


def compress_string(s):
    result = ""
    for char in sorted(set(s), key=s.index):  
        count = s.count(char)
        result += f"{char}{count}"
        return result

s = input("Enter a string: ")
compressed = compress_string(s)
print("Compressed string:", compressed)
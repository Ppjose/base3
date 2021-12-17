# Taking input from user
data = 'Welcome to GeeksForGeeks...'


# conversion Chart
conversion_code = {
	
	# Uppercase Alphabets
	'A': 1, 'B': 6, 'C': 10, 'D': 14, 'E': 18, 'F': 22,
	'G': 2, 'H': 7, 'I': 11, 'J': 15, 'K': 19, 'L': 23,
	'M': 3, 'N': 8, 'O': 12, 'P': 16, 'Q': 20, 'R': 24,
	'S': 4, 'T': 9, 'U': 13, 'V': 17, 'W': 21, 'X': 25,
	'Y': 26, 'Z': 27,

	# Lowercase Alphabets
	#'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u',
	#'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o',
	#'m': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i',
	#'s': 'h', 't': 'g', 'u': 'F', 'v': 'e', 'w': 'd', 'x': 'c',
	#'y': 'b', 'z': 'a'
    
}
# Creating converted output
converted_data = 0


for i in range(0, len(data)):
    
	if data[i] in conversion_code.keys():


		converted_data += conversion_code[data[i]]


	else:
		converted_data += data[i]

# Printing converted output
print(converted_data)

import sys
dict = []

def dict_setup(file):
	file = open(file, "r")
	for line in file:
		dict.append(line.strip())

def strspaceback(line):
	if line in dict:
		print("this line is a singular word:", line)
		return True
	
	print("len of line to start:", len(line))
	i = 0;
	while (i < len(line) + 1):
		#print("len of line:", len(line))
		#print("current i:", i)
		searchline = len(line) - i
		#print("currently searching:", line[searchline:])
		'''
		j = i
		endline = len(line) - j
		'''
	
		if line[searchline:] in dict:
			print("the end of this line is a word:", line[searchline:])
			#i += len(line) - i
			#print("line after finding end word:", line[:searchline])
			line = line[:searchline]
			i = 0;
		i += 1;
	
	if len(line) == 0:
		print("Worked backwards")
		return True

	else:
		print("failed backwards")
		return False


def strspacefore(line):
	if line in dict:
		print("this line is a singular word:", line)
		return True
	i = 0
	while (i < len(line) + 1):
		searchline = i
	
		if line[:searchline] in dict:
			print("the start of this line is a word:", line[:searchline])					
			line = line[searchline:]
			i = 0;
		i += 1;
	if len(line) == 0:
		print("Worked forewords")
		return True

	else:
		print("failed forewords")
		return False


def split(i):
	pass

def driver():
	num_lines = int(sys.stdin.readline().strip())
	for i in range(num_lines):
		x = sys.stdin.readline().strip()
		passfail = strspaceback(x)
		print("pass or failed: ", passfail)
		strspacefore(x)





if __name__ == "__main__":
	dict_setup('diction10k.txt')
	driver()
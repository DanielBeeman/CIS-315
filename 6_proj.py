import sys
dict = []

def dict_setup(file):
	file = open(file, "r")
	for line in file:
		dict.append(line.strip())

def strspace(line):
	if line in dict:
		print("this line is a singular word:", line)
		return True
	for i in range(len(line)+1):
		print("outer i: ",i)
		if line[:i] in dict:
			print("the first part is a word:", line[:i])
			#i += len(line[:i])
			for j in range(i, len(line)+1):
				print("line:", line[:5], "len of line + 1:", len(line)+1, "i is:", i, "j is:", j)

				#So if we want to go from the end to the start of a word,
				#say we have the word: 'licklake'
				#we want to take len((line)+1) - (i+j) and see if that is a word
				#from the end of the string

				if line[i:j] in dict:
					print("this next part is a word:", line[i:j])
					i += len(line[i:j])
			break
			#i += len(line[:i])


def split(i):
	pass

def driver():
	num_lines = int(sys.stdin.readline().strip())
	for i in range(num_lines):
		x = sys.stdin.readline().strip()
		strspace(x)
		





if __name__ == "__main__":
	dict_setup('diction10k.txt')
	driver()

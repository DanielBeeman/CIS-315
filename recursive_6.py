import sys
dict = {}

def dict_setup(file):
	file = open(file, "r")
	for line in file:
		dict[line.strip()] = 1

words = {}
def strspace(line):

	#base cases
	#this first if statement in particular 
	#should save some time by returning previously found words quicker.
	if line in words:
		return line
	if line in dict:
		return line

	i = 0
	while (i < len(line)):
		y = line[:i] 
		if (y in dict):
			words[i] = y
			x = strspace(line[i:])
			#we must check for None because otherwise, the current line isn't a word.
			if (x != None):
				#after hitting the base cases, we return back through the recursive calls.
				return (y + " " + x)
		i += 1
	return None



def driver():
	num_lines = int(sys.stdin.readline().strip())
	print() #for clarity
	for i in range(num_lines):
		x = sys.stdin.readline().strip()
		y = strspace(x)
		print("phrase number: ", (i+1))
		print(x) #the line we will be checking
		print("memoized attempt:")

		if (y != None):
			print("YES, can be split")	
			print(y)
		
		else:
			print("NO, cannot be split")
		print()



if __name__ == "__main__":
	dict_setup('diction10k.txt')
	driver()
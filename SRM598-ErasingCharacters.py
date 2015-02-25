# problem statement @ http://community.topcoder.com/stat?c=problem_statement&pm=12863&rd=15710

def EraseCharacters(string):
	#self.string = string
	for i in range(1,len(string)):
		if string[i] == string[i+1]:
			string = string[:i]+string[:i+1]

	return string


EraseCharacters("HelloWorld")

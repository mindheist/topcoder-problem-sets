def getanswer(string):
	#print string
	for element in string:
		if element != 'C' and element!='A' and element != 'T':
			string = string.replace(element,"")
			#print string
	if string == 'CAT': return "possible" 
	else: return "impossible"

print "for string HelCloA " , getanswer("HelCloA")
print "for string SGHDJHFIOPUFUHCHIOJBHAUINUIT " , getanswer("SGHDJHFIOPUFUHCHIOJBHAUINUIT")
print "for string ACBBAT", getanswer("ACBBAT")
print "for string CCCATT" , getanswer("CCCATT")

def reverse(s):



	string = list(s)


	i=0
	while i < (len(string) - 1 - i):
		temp = string[i]
		string[i] = string[len(string)-1 -i]
		string[len(string)-1 -i] = temp
		i+=1

	return ''.join(string)




string = "absdfsc"
print reverse(string)
class Solution:

    def Unique(self,string):
    	if string is None:
    		return True

    	if string == []:
    		return True

    	for i in range(len(string)-1):
    		if string[i] == string[i+1]:
    			return False


    	return True



A = Solution()

string= "AAABCB"
        

class String:
    def __init__(self):
        self.string = ''

    def getString(self):     		#Method 1
        self.string = str(input())

    def printString(self):   		#Method 2
        print(self.string.upper())

upper_case = String()  	     	#Input was all upper case (a)
lower_case = String()	       	#Input was all lower case (b)
upper_lower_case = String()	#Input was a mix of upper & lower case (c)

upper_case.getString()
upper_case.printString()

lower_case.getString()
lower_case.printString()

upper_lower_case.getString()
upper_lower_case.printString()

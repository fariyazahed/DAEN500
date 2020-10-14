first_num = int(input()) 	# Set first number of range
last_num = int(input()) 	# Set last number of range

while first_num <= last_num:
    if (first_num % 7) == 0 and (first_num % 5) != 0:
        print("{} is divisible by 7 but is not a multiple of 5.".format(first_num))
    first_num += 1

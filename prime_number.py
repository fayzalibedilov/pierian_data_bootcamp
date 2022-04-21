num = input()
if num > 1:
    for i in range(2, int(num/2)+1):
	if num % i == 0:
	    return False
	    break
	else:
	    return True
else:
    False

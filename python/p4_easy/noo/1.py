item = [1,2.4, {4,5}]
key = [2.2, 1,{4.5}]

for k in key:
	for i in item:
	    if k == i:
		print "found " , k
		break	
	else:
	    print "not found"


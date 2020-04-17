i = int(input())
for num in range(i):
	a,b,c = map(int,raw_input().split())
	if(c == 1):
		print "%.2d:%.2d - A porta abriu!" %(a,b) 
	else:
		print "%.2d:%.2d - A porta fechou!" %(a,b) 

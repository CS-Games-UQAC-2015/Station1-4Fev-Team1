#taper "python main.py" dans le Power Shell pour runner
#!/usr/bin/python


#Input
file = open("A-small-practice.in", encoding='utf-8')
T = int(file.readline())#Number of cases

outlets = []
for i in range(1, T): #Go through all cases

	N = file.read(0) #Number of outlets
	L =  0#Length of current in outlets
	outlets.append([])
	print(N)


file.close()


#Output
x = 1 #case number
y = 0 #minimum number of switches to charge all devices
print ("Case #" + str(x) + ": " + str(y))
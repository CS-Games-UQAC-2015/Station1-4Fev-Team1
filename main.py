#taper "python main.py" dans le Power Shell pour runner
#!/usr/bin/python

# WHAT IS DONE :
#   OUTPUT et INPUT

# WHAT TO BE DONE : 
#   LOGIC


#Input
file = open("A-small-practice.in")
T = int(file.readline())#Number of cases

outlets = []
flows = []

for i in range(1, T+1): #Go through all cases

	N, L= file.readline().split(" ") #Number of outlets
	# Cast N et L en int
	N = int(N) 
	L = int(L)
	
	outlets = file.readline().split(" ") # Table of all N Outlets
	flows = file.readline().split(" ") # Table of all N Flows
	
	#LOGIC GOES HERE :
    #use N, L, outlets and flows variable to find algorithm
	
	
	#Output
	y = 0 #minimum number of switches to charge all devices
	# If not possible, y must equal : "NOT POSSIBLE"
	print ("Case #" + str(i) + ": " + str(y)) 


file.close()



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
 solutionFind = False
 #continuefor = True
 outlets.sort()
 flows.sort()

 #for it1 in range(1, N+1):
  #if outlets[it1]==flows[it1]:
   #continuefor = True
  #else:
  # continuefor=False
   #break







	#Output
 y = 0 #minimum number of switches to charge all devices
	# If not possible, y must equal : "NOT POSSIBLE"
 if solutionFind:
  print ("Case #" + str(i) + ": " + str(y))
 else:
  print ("Case #" + str(i) + ": " + "NOT POSSIBLE")

 print (" Scusez les gars j'ai essayer d'hardcoder pleins de truc pi jconnais pas le langage faique allez toute chier on aura failer cette épreuve la !!")


file.close()




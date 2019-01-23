import subprocess 

world = 1

member = [2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,
44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,65,66,67,68,69,70,73,74,75,76,77,78,86,87,88,89,90,91,92,
95,96,115,116,120,121,122,124,128,129,144,145,146,147,148,149,150,164,165,166,167,191,192,193,194,195,196,213,214,215,
216,217,218,219,220,221,222,223,224,225]

free = [1,8,16,26,71,72,79,80,81,82,83,84,85,93,94,97,98,99,113,114,117,118,119,125,126,127,130,131,132,133,134,135,
136,137,138,139,140,151,152,153,154,155,156,157,158,159,168,169,170,171,172,173,174,175,176,177,197,198,199,200,201,
202,203,204]

best_ping = 1000

best_world = 0

while world < 226:
	if 87 <= world <+ 92:
		world = 93
	if 100 <= world <= 112:
		world = 113
	if 122 <= world <= 127:
		world = 128

	op = subprocess.check_output(["ping", "oldschool"+str(world)+".runescape.com", "-n", "1"]) #ping function
	
	
	#Find the average from the ping command
	op = str(op)
	start = op.find("Average")
	end = len(op)-1
	#Extract the number itself
	ping = int(''.join(filter(str.isdigit, op[start:end-4])))
	
	#Compare to the best_ping
	if ping < best_ping:
		best_ping = ping	
		best_world = world + 300
	
	print("World "+str(world+300)+": "+op[start:end-4])
	
	world = world + 1

print("Best World is World "+str(best_world)+" with ping = "+str(best_ping)+"ms!")
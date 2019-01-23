import subprocess 

world = 1



while world < 226:
	if 87 <= world <+ 92:
		world = 93
	if 100 <= world <= 112:
		world = 113
	if 122 <= world <= 127:
		world = 128

	op = subprocess.check_output(["ping", "oldschool"+str(world)+".runescape.com", "-n", "1"])
	
	op = str(op)
	start = op.find("Average")
	end = len(op)-1
	
	print("World "+str(world+300)+": "+op[start:end-4])
	
	world = world + 1
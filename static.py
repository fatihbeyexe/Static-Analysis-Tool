import sys
import os
import potentialList
scriptPath=os.path.abspath(sys.argv[0])
blackListPath=scriptPath[:-9]+"blacklist/blacklist.txt"
try:
	exePath=sys.argv[1]
	if(sys.argv[1]== "-h"):
		print("Example usage: python static.py Sample.exe")
		exit()
except IndexError:
	print("Wrong parameters, for usage type [-h]")
	exit()
os.system("strings "+exePath+" > blacklist/strings.txt")
blacklist=open(blackListPath,"r")
blackArray=blacklist.read().splitlines()
stringsTxt=open(scriptPath[:-9]+"blacklist/strings.txt","r")
stringsArray=stringsTxt.read().splitlines()
potential=""
for i in range(len(stringsArray)):
	for j in range(len(blackArray)):	
		if( blackArray[j]==stringsArray[i]):
			if(j>0 and j<12):
				potential=potential+"A"
			elif(j>12 and j<19):
				potential=potential+"B"
			elif(j>19 and j<24):
				potential=potential+"C"
			elif(j>24 and j<29):
				potential=potential+"D"
			elif(j>29 and j<32):
				potential=potential+"E"
			elif(j>32 and j<35):
				potential=potential+"F"
			elif(j>35 and j<38):
				potential=potential+"G"
			elif(j>38 and j<44):
				potential=potential+"H"
			elif(j>44 and j<60):
				potential=potential+"I"
			elif(j>60 and j<64):
				potential=potential+"J"
			elif(j>64 and j<67):
				potential=potential+"K"
			elif(j>67 and j<70):
				potential=potential+"L"
			elif(j>70 and j<73):
				potential=potential+"M"
potentialList.listing(potential)
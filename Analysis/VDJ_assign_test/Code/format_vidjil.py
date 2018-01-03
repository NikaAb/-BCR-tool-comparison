from collections import Counter
import sys

#=======================================================================================
###Global variables
fastaFile = ""
#Usage
usage = "python readvidjilcloneout.py -f fastaFile\n"
#=======================================================================================
### Read parameters
def readParameters(args):
	global fastaFile
	for i in range(1,len(args)):
		if (args[i] == "-f"):
			fastaFile = args[i+1]
		elif (args[i] == "-h"):
			print usage
#=======================================================================================
### Check parameters
def checkParameters():
	if (fastaFile == ""):
		print "ERROR::Parameter -f fastaFile is required"
		sys.exit(1);
#=======================================================================================

def read(nomfichier):
	listresult=[]
	cloneNum="C"+(nomfichier.split("-")[1])+"\t"
	print cloneNum
	file=open(nomfichier,"r")
	lines=file.readlines()
	file.close()
	for l in lines:
		if l[0:2]==">S":
			m=l.split("|")
			M=m[0]
			listresult.append(M)
	return listresult,cloneNum
#=======================================================================================
def writetofile(dico,cloneNum):
	filetowrite=open("outvidjil.txt","a")
	filetowrite.write(cloneNum)
	for m in range(len(listresult)):		
		filetowrite.write(str(listresult)+" ")
	return "0"
#=======================================================================================
#										Main
#=======================================================================================

readParameters(sys.argv)
checkParameters()
listresult,cloneNum=read(fastaFile)
writetofile(listresult,cloneNum)


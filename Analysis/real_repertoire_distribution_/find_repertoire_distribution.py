import sys
########################################################################
###Global variables
vidjil_clone_output_file = ""
name_file_1= ""
name_file_2 = ""


#Usage
usage = "python find_repertoire_distribution.py [options] -f vidjil_clone_output_file -g name_file_1 -o name_file_2 \n"

########################################################################
### Read parameters
def readParameters(args):
	global vidjil_clone_output_file
	global name_file_1
	global name_file_2
	for i in range(1,len(args)):
		if (args[i] == "-f"):
			vidjil_clone_output_file = args[i+1]
		elif (args[i] == "-g"):
			name_file_1 = args[i+1]
		elif (args[i] == "-o"):
			name_file_2 = args[i+1]
		elif (args[i] == "-h"):
			print usage
########################################################################
### Check parameters
def checkParameters():
	if (vidjil_clone_output_file == ""):
		print "ERROR::Parameter -f vidjil_clone_output_file is required\n"
		sys.exit(1);
	elif (name_file_1 == ""):
		print "ERROR::Parameter -g name_file_1 is required\n"
		sys.exit(1);
	elif (name_file_2 == ""):
		print "ERROR::Parameter -o name_file_2 is required\n"
		sys.exit(1);
	
########################################################################
def read_output_file(filename):
	f=open(filename,"r")
	lines=f.readlines()
	f.close()
	return lines

########################################################################
def write_clone_file(vidjil_clone_output_file):
	lines=read_output_file(vidjil_clone_output_file)
	total_number_read=0
	for l in lines:
		listloc=[]
		if l[0]==">":
			split=l.split("\t")
			number_of_read=int(split[0].split("--")[2])
			
			if len(split)==3:# have a defind V and J
				total_number_read+=number_of_read 
				V,J,CDR3=split[2].split(" ")[0],split[2].split(" ")[2],split[2].split(" ")[-1][:-2]
				if "/" in CDR3:
					CDR3="_"
			write_output_file([number_of_read,V,J,CDR3],name_file_1)
	return total_number_read
		
########################################################################						
def write_output_file(list_to_write,name):
	f=open(name,"a")
	for item in list_to_write:	
		f.write(str(item)+"\t")
	f.write("\n")
	f.close()
	return 0
########################################################################

def distribution(total_number_read):
	dico_clone={}
	lines=read_output_file(name_file_1)
	for l in lines:
		split=l.split("\t")
		key=str(split[1])+"_"+str(split[2])
		if key in dico_clone.keys():
			dico_clone[key].append(int(split[0]))
		else:
			dico_clone[key]= [int(split[0])]
	for key in dico_clone.keys(): 
		write_output_file([sum(dico_clone[key])/float(total_number_read)],name_file_2)
	return 0
	
########################################################################
#####################         Main      ################################
########################################################################
readParameters(sys.argv)
checkParameters()
total_number_read=write_clone_file(vidjil_clone_output_file)
distribution(total_number_read)

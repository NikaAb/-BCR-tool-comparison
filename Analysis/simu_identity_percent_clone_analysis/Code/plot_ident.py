import sys
import matplotlib.pyplot as plt
import numpy as np

########################################################################
###Global variables
family_file = ""
identity_file = ""


#Usage
usage = "python plot_ident.py [options] -f family_file -g identity_file\nwhere basic options are:\n"

########################################################################
### Read parameters
def readParameters(args):
	global family_file
	global identity_file

	for i in range(1,len(args)):
		if (args[i] == "-f"):
			family_file = args[i+1]
		elif (args[i] == "-g"):
			identity_file = args[i+1]
		elif (args[i] == "-h"):
			print usage
########################################################################
### Check parameters
def checkParameters():
	if (family_file == ""):
		print "ERROR::Parameter -f family_file is required\n"
		sys.exit(1);
	elif (identity_file == ""):
		print "ERROR::Parameter -g identity_file is required\n"
		sys.exit(1);
	
########################################################################
def read_output_file(filename):
	f=open(filename,"r")
	lines=f.readlines()
	f.close()
	return lines




########################################################################
def make_dico_identity(identity_file):
	dico_identity={}
	identity=read_output_file(identity_file)
	compt=0
	for l in identity:
		print compt,"/",len(identity)
		split=l.split("\t")
		if split[0] in dico_identity.keys():
			
			dico_identity[split[0]][split[1]]=split[2]
		else:
			dico_identity[split[0]]={}
			dico_identity[split[0]][split[1]]={}
			dico_identity[split[0]][split[1]]=split[2]
		if split[1] in dico_identity.keys():
			
			dico_identity[split[1]][split[0]]=split[2]
		else:
			dico_identity[split[1]]={}
			dico_identity[split[1]][split[0]]={}
			dico_identity[split[1]][split[0]]=split[2]
		compt+=1
	#print dico_identity
	return dico_identity
				
########################################################################
def make_dico_family(family_file):
	dico_family={}
	family=read_output_file(family_file)
	for l in family:
		#print l.split("\t")
		group=l.split("\t")[0]
		seq=l.split("\t")[1].split(" ")
		#print seq
		for s in range(len(seq)-1):
			
			dico_family[seq[s]]=group
	#print dico_family
	return dico_family
########################################################################
def seperate_values(dico_identity,dico_family):
	inter_family=[]
	intra_family=[]
	list_seq=dico_family.keys()	
	for i in range(len(list_seq)-1):
		for j in range(i,len(list_seq)):
			print i,j
			if dico_family[list_seq[i]]==dico_family[list_seq[j]]:

				if list_seq[i] in dico_identity.keys()   :

					if list_seq[j] in dico_identity[list_seq[i]].keys():
						intra_family.append(float(dico_identity[list_seq[i]][list_seq[j]]))
				elif list_seq[j] in dico_identity.keys():
					if list_seq[i] in dico_identity[list_seq[j]].keys():
						intra_family.append(float(dico_identity[list_seq[j]][list_seq[i]]))
				
			else:

				if list_seq[i] in dico_identity.keys() :

					if list_seq[j] in dico_identity[list_seq[i]].keys():
						inter_family.append(float(dico_identity[list_seq[i]][list_seq[j]]))
					
				elif list_seq[j] in dico_identity.keys():

					if list_seq[i] in dico_identity[list_seq[j]].keys():
						inter_family.append(float(dico_identity[list_seq[j]][list_seq[i]]))

	return sorted(inter_family),sorted(intra_family)

########################################################################
def plot(inter_family,intra_family):
	plt.hist(inter_family, weights =range(len(inter_family)),  color = 'yellow', edgecolor = 'red', hatch = '/', label = 'interfamily',rwidth = 0.8,align = 'left')
	plt.hist(intra_family, weights=range(len(intra_family)),color = 'green', edgecolor = 'blue', hatch ='-' , label = 'intrafamily',rwidth = 0.8,alpha = 0.5,align = 'left')
	#plt.hist(inter_family, bins = range(10),  color = 'yellow', edgecolor = 'red', hatch = '/', label = 'interfamily',rwidth = 0.8)
	#plt.hist(intra_family, bins = range(10),color = 'green', edgecolor = 'blue', alpha = 0.5, hatch ='-' , label = 'intrafamily',rwidth = 0.8)
	plt.ylabel('# sequence pair')
	plt.xlabel('identity %')
	plt.title(' Partis ')
	plt.legend()
	plt.show()
	return 0
		

########################################################################
#####################         Main      ################################
########################################################################
readParameters(sys.argv)
checkParameters()
dico_identity=make_dico_identity(identity_file)
dico_family=make_dico_family(family_file)
inter_family,intra_family=seperate_values(dico_identity,dico_family)
plot(inter_family,intra_family)

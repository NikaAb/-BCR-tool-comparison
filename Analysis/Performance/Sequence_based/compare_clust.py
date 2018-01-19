"""
This script compares real clusters and predicted clusters content and measure 
precision and recall.

The comparison is based on method explained in method file. 

True cluster's file and predicted cluster's file have the same format:

C1	C1_a C1_b
C2	C1_c C2_e
C3	C2_d

The first column shows the cluster label and the second one represents sequences 
in that cluster, separated by space.
Two columns are seperated by \t.
"""


import sys
from collections import Counter 	
#===================================================================================
#Global variables
Real_cluster = ""
Predicted_cluster = ""


#Usage
usage = "python compare_clust.py [options] -r Real_cluster -p Predicted_cluster \n"

#===================================================================================
#Read parameters
def readParameters(args):
	global Real_cluster
	global Predicted_cluster

	for i in range(1,len(args)):
		if (args[i] == "-f"):
			Real_cluster = args[i+1]
		elif (args[i] == "-g"):
			Predicted_cluster = args[i+1]
		elif (args[i] == "-h"):
			print usage
#===================================================================================
### Check parameters
def checkParameters():
	if (Real_cluster == ""):
		print "ERROR::Parameter -f Real_cluster is required\n"
		sys.exit(1);
	elif (Predicted_cluster == ""):
		print "ERROR::Parameter -g Predicted_cluster is required\n"
		sys.exit(1);

#===================================================================================
def read_output_file(filename):
	f=open(filename,"r")
	lines=f.readlines()
	f.close()
	return lines
#===================================================================================
def creat_hashtrue(lines):
	HashTrue={}		
	for l in lines:
		label=l.split("\t")[0]
		sequences=l.split("\t")[1].split(" ")
		HashTrue[label]=len(sequences)
	return HashTrue
#===================================================================================
def getlabel(seqName):
	return seqName.split("_")[0]
#===================================================================================
def read_hashpredict(lines):
	HashPredict={} # contains lables of each cluster
	seq_dico={}  # contains sequences of each cluster
	for l in lines: 
		label=l.split("\t")[0]
		sequences=l.split("\t")[1][:-1].split(" ")
		seq_dico[label]=sequences
		for s in sequences:
			if label in HashPredict.keys():
				HashPredict[label].append(getlabel(s))
			else:
				HashPredict[label]=[getlabel(s)]
		HashPredict[label]=dict(Counter(HashPredict[label]))
	return HashPredict,seq_dico

#===================================================================================
def counter(seq_dico,HashTrue,HashPredict):
	TP,FN,FP=0,0,0
	for key in seq_dico.keys():
		tp,fn,fp=0,0,0
		for s in seq_dico[key]:
			tp=int(HashPredict[key][getlabel(s)])-1
			fn=int(HashTrue[getlabel(s)])-1-tp
			for c in HashPredict[key].keys():
				if c !=getlabel(s):
					fp=int(HashPredict[key][c])		
			TP+=tp
			FN+=fn
			FP+=fp
	return TP,FN,FP
#===================================================================================
def Classiq_mesure(TP,FN,FP):
	print "Recall : ",TP/float(TP+FN)
	print "Precision : ", TP/float(TP+FP)
	return 0
#===================================================================================
def precision_recall(Predicted_cluster,Real_cluster):
	predicted_lines=read_output_file(Predicted_cluster)
	real_lines=read_output_file(Real_cluster)
	HashTrue=creat_hashtrue(real_lines)
	HashPredict,seq_dico=read_hashpredict(predicted_lines)
	TP,FN,FP=counter(seq_dico,HashTrue,HashPredict)
	Classiq_mesure(TP,FN,FP) 
	return 0			
#===================================================================================
#			    		Main
#===================================================================================
readParameters(sys.argv)
checkParameters()
precision_recall(Predicted_cluster,Real_cluster)

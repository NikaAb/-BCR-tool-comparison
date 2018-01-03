def read_output_file(filename):
	f=open(filename,"r")
	lines=f.readlines()
	f.close()
	return lines

def filterName(lines):
	dicoseqNumID={}
	for l in range(1,len(lines)):
		ID,NUM= lines[l].split("\t")[-13],lines[l].split("\t")[-11]
		seqNum=lines[l].split("\t")[0]
		seqID=lines[l].split("\t")[1].split("|")[0]
		#if "|" not in lines[l].split("\t")[1]:
			#seqID=lines[l].split("\t")[1].split("_")[0]
		#else:
			#seqID=lines[l].split("\t")[1].split("|")[0]
		dicoseqNumID[seqNum]= seqID
	
	return dicoseqNumID


def filterCloneID(lines):
	dicoCloneSeq={}
	for l in range(1,len(lines)):
		NumClone= lines[l].split("\t")[1].split("-")[0]
		Seq=lines[l].split("\t")[6]
		print Seq.split(" ")
		dicoCloneSeq[NumClone]=Seq.split(" ")
	return dicoCloneSeq





def Vquest_format(listNomSeq,listCloneId):
	filetowrite=open("outVquest.txt","w") #outMixcrnotfinished.txt
	for c in listCloneId.keys():
		ClusterNum="C"+str(c)+"\t"
		filetowrite.write(ClusterNum)
		member=listCloneId[c]
		for m in range(len(member)):
			if member[m]  in listNomSeq.keys():
				#print member[m]
				filetowrite.write(str(listNomSeq[member[m]])+" ")
			#else:
				#filetowrite.write(str(listNomSeq[member[m]])+" ")
		filetowrite.write("\n")
	return 0
	

def creatdico(lines):
	dico={}
	for l in range(1,len(lines)):
		SeqID=lines[l].split("\t")[0]
		CloneID=lines[l].split("\t")[1][:-1]
		if CloneID in dico.keys():
			dico[CloneID].append(SeqID)
		else:
			dico[CloneID]=[SeqID]
	return dico

def writedico(dico):
	filetowrite=open("outmixcrMap.txt","w")
	for c in dico.keys():
		ClusterNum="C"+str(c)+"\t"
		filetowrite.write(ClusterNum)
		member=dico[c]
		for m in range(len(member)):
			filetowrite.write(str(member[m])+" ")
		filetowrite.write("\n")
	return 0	

listNom=read_output_file("allData.txt")
listSeqNumID=filterName(listNom)


#CloneID=read_output_file("stats_30000_simulated_S30000_IGH.txt")
#listCloneId=filterCloneID(CloneID)


#Vquest_format(listSeqNumID,listCloneId)

"""
IDs=read_output_file("outMixcr.txt")
dico=creatdico(IDs)
writedico(dico)
"""

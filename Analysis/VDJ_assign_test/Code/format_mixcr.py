def read_output_file(filename):
	f=open(filename,"r")
	lines=f.readlines()
	f.close()
	return lines

def filterName(lines):
	listNomSeq =[]
	for l in lines:
		if l[0] ==">":
			listNomSeq.append(l.split("|")[0][1:])
	return listNomSeq


def filterCloneID(lines):
	listCloneId=[]
	for l in lines:
		if l[0:3] != "dro":
			listCloneId.append(l.split(":")[0])
		else:
			listCloneId.append("dropped")
	return listCloneId



def Mixcr_format(listNomSeq,listCloneId):
	filetowrite=open("out_final_mixcr_simulated_30000.txt","w") #outMixcrnotfinished.txt
	filetowrite.write("SequenceID	CloneID")
	for c in range(len(listNomSeq)):
		filetowrite.write("\n")
		line=str(listNomSeq[c])+"\t"+str(listCloneId[c])
		filetowrite.write(line)
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

listNom=read_output_file("clones.seq30000.fasta")
listNomSeq=filterName(listNom)


CloneID=read_output_file("alignmixcr.txt")
listCloneId=filterCloneID(CloneID)


Mixcr_format(listNomSeq,listCloneId)


IDs=read_output_file("outMixcr.txt")
dico=creatdico(IDs)
writedico(dico)

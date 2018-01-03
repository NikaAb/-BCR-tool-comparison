from collections import Counter



def cvs2txt(cvsfile,txtfile):
	try:
   		my_input_file = open(cvsfile, "r")
	except IOError as e:
    		print("I/O error({0}): {1}".format(e.errno, e.strerror))

	if not my_input_file.closed:
    		text_list = [];
    		for line in my_input_file.readlines():
        		line = line.split(",", 44)
        		text_list.append(" ".join(line))
    		my_input_file.close()

	try:
    		my_output_file = open(txtfile, "w")
	except IOError as e:
   		print("I/O error({0}): {1}".format(e.errno, e.strerror))
	if not my_output_file.closed:
    		for line in text_list:
        		my_output_file.write("  " + line)
   		print 'File Successfully written.'
    		my_output_file.close()
	return 0




def read_output_file(filename):
	f=open(filename,"r")
	lines=f.readlines()
	f.close()
	return lines



def partis_format(lines):
	print "ok"
	filetowrite=open("outPartis.txt","w")
	print len(lines)
	a=lines[1].split(" ")
	clones=a[5].split(";")
	for c in range( len(clones)):
		ClusterNum="C"+str(c)+"\t"
		filetowrite.write(ClusterNum)
		member=clones[c].split(":")
		#filetowrite.write((str(len(member))+"\t"))
		for m in range(len(member)):
			filetowrite.write(str(member[m])+" ")
		
		filetowrite.write("\n")
		
		











"""
def partis_format(lines):
	dico={}
	a=lines[1].split(" ")[5][:-2].split(";")
	for i in range(len(a)):
		member= a[i].split(":")
		#cluster= "group_%d" %(i)		
		dico[i+1]=[]
		for j in range(len(member)):
			dico[i+1].append(member[j])
	return dico
"""
def readpartis(lines):
	DicoRes={}
	for l in range(1,len(lines)):
		split=lines[l].split(" ")
		DicoRes[split[2]]=[split[3],split[4],split[5]]
	return DicoRes

def calcule_partis(dicopartis,dicoseq):
	filetowrite=open("outPartis_OSR535-1_S18.txt","w")
	for key in dicopartis.keys():
		#print key
		cloneNum="C"+str(key)
		#print cloneNum
		listseq=[]
		for seq in dicopartis[key]:
			listseq.append(str(dicoseq[seq]))
		dico_count=dict(Counter(listseq))
		#print dico_count
		for key2 in dico_count.keys():
			gene= key2.split("'")
			line=cloneNum+"\t"+gene[1]+"\t"+gene[3]+"\t"+gene[5]+"\t"+str(dico_count[key2])+"\n"
			filetowrite.write(str(line))
			
		
			
			
		
cvs2txt("30000simulatedclones.csv","clone_Partis.txt")
lines=read_output_file("clone_Partis.txt")
partis_format(lines)

"""
cvs2txt("sw-cache-687934555035221418.csv","clone_Partis_OSR535-1_S18_partition.tx")


lines=read_output_file("clone_Partis_OSR535-1_S18.txt")
dicopartis=partis_format(lines)

lines2=read_output_file("clone_Partis_OSR535-1_S18_partition.tx")
dicoseq=readpartis(lines2)

calcule_partis(dicopartis,dicoseq)



"""














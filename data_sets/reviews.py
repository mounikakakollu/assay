f1=open("video_re.txt","r").read()
f1=f1.split("\n")
#length=(len(f1)*30)/100
f2=open("video.txt","w")
for i in range(len(f1)):
	f1[i]=f1[i][f1[i].find(" ")+1:]
	f2.write(str(f1[i])+"\n")
f2.close()
#f2=open("video.txt","w")
#for i in range(length,len(f1)):
#	f2.write(str(f1[i])+"\n")
#f2.close()
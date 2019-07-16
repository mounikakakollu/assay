f=open("../data_sets/baby/baby_test.txt","r").read()
f1=open("../data_sets/garden/garden_test.txt","r").read()
f2=open("../data_sets/music/music_test.txt","r").read()
f3=open("../data_sets/health/health_test.txt","r").read()
f4=open("../data_sets/video/video_test.txt","r").read()
f=f.split("\n")
f1=f1.split("\n")
f2=f2.split("\n")
f3=f3.split("\n")
f4=f4.split("\n")
from domain import *
limit=500
while(True):
	t=0
	f5=open("../test.txt","w")
	for i in range(len(f)):
		if(i==limit):
			break;
		else:
			f5.write(f[i]+"\n")
			t=1
	for j in range(len(f1)):
		if(j==limit):
			break
		else:
			f5.write(f1[j]+"\n")
			t=1
	for k in range(len(f2)):
		if(k==limit):
			break
		else:
			f5.write(f2[k]+"\n")
			t=1
	for l in range(len(f3)):
		if(l==limit):
			break
		else:
			f5.write(f3[l]+"\n")
			t=1
	for m in range(len(f4)):
		if(m==limit):
			break
		else:
			f5.write(f4[m]+"\n")
			t=1
	if(t==1):
		limit+=500
		print "Now test file is ready"
		startclassification()
	else:
		break

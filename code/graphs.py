import matplotlib.pyplot as plt
lables='positive','Negative','Neutral'
f=open("result.txt","r").read()
f=f.split("\n")
count={}
#for i in f:
#	index=str(i).find(" ")
#	m=i[:index]
#	if(m not in count):
#		count.setdefault(m,{})
#		count[m].setdefault('Positive',0)
#		count[m].setdefault('Negative',0)
#		count[m].setdefault('Neutral',0)
	#print reviews[i]
#	if(i[index+1:]=='Positive'):
#		count[m]['Positive']+=1
#	elif(i[index+1:]=='Neutral'):
#		count[m]['Neutral']+=1
#	else:
#		count[m]['Negative']+=1
#id_no=raw_input("Enter product id\n")
#if(id_no in count):
#	sizes =[count[id_no]['Positive'],count[id_no]['Negative'],count[id_no]['Neutral']]
#	print count['B0016KV73W']
#	colors=['pink','green','yellow']
#	explode=(0,0,0)
#	plt.pie(sizes,labels=lables,colors=colors,autopct='%1.1d%%',shadow=True, startangle=140)
#	plt.show()
# TOTAL POLARITY GRAPH
count.setdefault('Negative',0)
count.setdefault('Positive',0)
count.setdefault('Neutral',0)
for i in f:
	if(i==''):
		continue
	index=str(i).find(" ")
	if(i[index+1:]=='Positive'):
		count['Positive']+=1
	elif(i[index+1:]=="Neutral"):
		count['Neutral']+=1
	else:
		count['Negative']+=1
print count
sizes=[count['Positive'],count['Negative'],count['Neutral']]
colors=['orange','pink','green']
explode=(0.1,0,0)
plt.pie(sizes,labels=lables,colors=colors,autopct='%1.1d%%',shadow=True,startangle=160)
plt.show()
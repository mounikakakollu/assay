baby = open("../data_sets/baby/baby_re.txt").read();
baby = baby.split("\n")
garden = open("../data_sets/garden/garden_test.txt").read();
garden = garden.split("\n")
health = open("../data_sets/health/health_test.txt").read();
health = health.split("\n")
video = open("../data_sets/video/video_test.txt").read();
video = video.split("\n")
music = open("../data_sets/music/music_test.txt").read();
music = music.split("\n")
def CrossCheck(name,sentence,Evalution):
	#print Evalution
	if(name=="baby"):
		calculation(sentence,baby,name,Evalution)
	elif(name=="garden"):
		calculation(sentence,garden,name,Evalution)
	elif(name=="health"):
		calculation(sentence,health,name,Evalution)
	elif(name=="video"):
		calculation(sentence,video,name,Evalution)
	else:
		calculation(sentence,music,name,Evalution)
	return Evalution
def calculation(sentence,f,name,Evalution):
	if(sentence in f):
		Evalution["True_Positive"]+=1
	elif(sentence in baby and name!="baby") or (sentence in health and name!="health") or (sentence in garden and name!="garden") or (sentence in video and name!="video") or (sentence in music and name!="music"):
		Evalution["False_Negative"]+=1
	elif(sentence not in baby and name=="baby") or (sentence not in health and name=="health") or (sentence not in garden and name=="garden") or (sentence not in video and name=="video") or (sentence not in music and name=="music"):
		Evalution["False_Positive"]+=1
	else:
		Evalution["True_Negative"]+=1
	return Evalution
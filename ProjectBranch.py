import csv

datafile = open('Match.csv', 'r')
datareader = csv.reader(datafile,delimiter=',')
matchorder = []
for row in datareader:
	matchorder.append(row)

team1battingprobability = []
team1bowlingprobability = []
array1d = []
array2d = []

datafile = open('./ProfileData/BowlProfile.csv', 'r')
datareader = csv.reader(datafile,delimiter=',')
temp = []
for row in datareader:
	temp.append(row)

datafile = open('ClusterVCluster.csv', 'r')
datareader = csv.reader(datafile,delimiter=',')
tempcluster = []
for row in datareader:
	tempcluster.append(row)

datafile = open('./ClusterData/BatsmanClusterData.csv', 'r')
datareader = csv.reader(datafile,delimiter=',')
tempbatcluster = []
for row in datareader:
	tempbatcluster.append(row)

datafile = open('./ClusterData/BowlerClusterData.csv', 'r')
datareader = csv.reader(datafile,delimiter=',')
tempbowlcluster = []
for row in datareader:
	tempbowlcluster.append(row)

for i in xrange(1,len(matchorder[2])):
	if(matchorder[2][i]==''):
		break
	for j in xrange(1,len(temp)):
		if(matchorder[2][i]==temp[j][0]):
			array1d.append(matchorder[2][i])
			array1d.append(float(temp[j][11]))
			array1d.append(float(temp[j][11]))
			break
	team1bowlingprobability.append(array1d)
	array1d = []

for i in xrange(1,len(matchorder[3])):
	if(matchorder[3][i]==''):
		break
	datafile = open('./PlayerProbabilities/'+matchorder[3][i]+'.csv', 'r')
	datareader = csv.reader(datafile,delimiter=',')
	temp = []
	for row in datareader:
		temp.append(row)

	for l in xrange(1,len(tempbatcluster)):
		if(matchorder[3][i]==tempbatcluster[l][0]):
			batcluster=tempbatcluster[l][3]

	for j in xrange(0,len(team1bowlingprobability)):

		for l in xrange(1,len(tempbowlcluster)):
			if(team1bowlingprobability[j][0]==tempbowlcluster[l][0]):
				bowlcluster=tempbowlcluster[l][4]

		for k in xrange(1,len(temp)):
			if(matchorder[3][i]==temp[k][0]) and (team1bowlingprobability[j][0]==temp[k][1]):
				array1d.append(matchorder[3][i])
				array1d.append(team1bowlingprobability[j][0])
				if(temp[k][2]=='0.0'):
					for l in xrange(1,len(tempcluster)):
						if(batcluster==tempcluster[l][0]) and (bowlcluster==tempcluster[l][1]):
							array1d.append(float(tempcluster[l][2]))
							array1d.append(float(tempcluster[l][2]))	
				else:				
					array1d.append(float(temp[k][2]))
					array1d.append(float(temp[k][2]))
				if(temp[k][3]=='0.0'):
					for l in xrange(1,len(tempcluster)):
						if(batcluster==tempcluster[l][0]) and (bowlcluster==tempcluster[l][1]):
							array1d.append(float(tempcluster[l][3]))
							array1d.append(float(tempcluster[l][3]))	
				else:				
					array1d.append(float(temp[k][3]))
					array1d.append(float(temp[k][3]))
				if(temp[k][4]=='0.0'):
					for l in xrange(1,len(tempcluster)):
						if(batcluster==tempcluster[l][0]) and (bowlcluster==tempcluster[l][1]):
							array1d.append(float(tempcluster[l][4]))
							array1d.append(float(tempcluster[l][4]))	
				else:				
					array1d.append(float(temp[k][4]))
					array1d.append(float(temp[k][4]))
				if(temp[k][5]=='0.0'):
					for l in xrange(1,len(tempcluster)):
						if(batcluster==tempcluster[l][0]) and (bowlcluster==tempcluster[l][1]):
							array1d.append(float(tempcluster[l][5]))
							array1d.append(float(tempcluster[l][5]))	
				else:				
					array1d.append(float(temp[k][5]))
					array1d.append(float(temp[k][5]))
				if(temp[k][6]=='0.0'):
					for l in xrange(1,len(tempcluster)):
						if(batcluster==tempcluster[l][0]) and (bowlcluster==tempcluster[l][1]):
							array1d.append(float(tempcluster[l][6]))
							array1d.append(float(tempcluster[l][6]))	
				else:				
					array1d.append(float(temp[k][6]))
					array1d.append(float(temp[k][6]))
				if(temp[k][7]=='0.0'):
					for l in xrange(1,len(tempcluster)):
						if(batcluster==tempcluster[l][0]) and (bowlcluster==tempcluster[l][1]):
							array1d.append(float(tempcluster[l][7]))
							array1d.append(float(tempcluster[l][7]))	
				else:				
					array1d.append(float(temp[k][7]))
					array1d.append(float(temp[k][7]))
				if(temp[k][8]=='0.0'):
					for l in xrange(1,len(tempcluster)):
						if(batcluster==tempcluster[l][0]) and (bowlcluster==tempcluster[l][1]):
							array1d.append(float(tempcluster[l][8]))
							array1d.append(float(tempcluster[l][8]))
				else:				
					array1d.append(float(temp[k][8]))
					array1d.append(float(temp[k][8]))
				if(temp[k][9]=='0.0'):
					for l in xrange(1,len(tempcluster)):
						if(batcluster==tempcluster[l][0]) and (bowlcluster==tempcluster[l][1]):
							array1d.append(1-float(tempcluster[l][9]))
							array1d.append(float(tempcluster[l][9]))	
				else:				
					array1d.append(1-float(temp[k][9]))
					array1d.append(float(temp[k][9]))
				break
		if(len(array1d)==0):
			for l in xrange(1,len(tempcluster)):
				if(batcluster==tempcluster[l][0]) and (bowlcluster==tempcluster[l][1]):
					array1d.append(matchorder[3][i])
					array1d.append(team1bowlingprobability[j][0])
					array1d.append(float(tempcluster[l][2]))
					array1d.append(float(tempcluster[l][2]))
					array1d.append(float(tempcluster[l][3]))
					array1d.append(float(tempcluster[l][3]))
					array1d.append(float(tempcluster[l][4]))
					array1d.append(float(tempcluster[l][4]))
					array1d.append(float(tempcluster[l][5]))
					array1d.append(float(tempcluster[l][5]))
					array1d.append(float(tempcluster[l][6]))
					array1d.append(float(tempcluster[l][6]))
					array1d.append(float(tempcluster[l][7]))
					array1d.append(float(tempcluster[l][7]))
					array1d.append(float(tempcluster[l][8]))
					array1d.append(float(tempcluster[l][8]))
					array1d.append(1-float(tempcluster[l][9]))
					array1d.append(float(tempcluster[l][9]))
		array2d.append(array1d)
		array1d = []
	team1battingprobability.append(array2d)
	array2d = []



#for i in xrange(0,len(team1battingprobability)):
#	for j in xrange(0, len(team1battingprobability[i])):
#		print (team1battingprobability[i][j])

#for i in xrange(0,len(team1bowlingprobability)):
#	print (team1bowlingprobability[i])

print"\n\n1st INNINGS :  "+matchorder[6][2]
team1runs=0
strike = 1
nonstrike = 2
team1balls = 0
team1overs = 0
team1wickets = 0
for i in xrange(1,21):
	bowler = 0
	for j in xrange(0,len(team1bowlingprobability)):
		if(team1bowlingprobability[j][0]==matchorder[1][i]):
			bowler = j
	out = 0
	team1balls = 0
	perballplay = 0
	for j in xrange(1,7):
		if(team1bowlingprobability[bowler][1]>=team1battingprobability[strike-1][bowler][16]):
			out = 1
			team1wickets = team1wickets+1
			team1bowlingprobability[bowler][1] = team1bowlingprobability[bowler][1]/5
			team1balls = team1balls+1
			print "\n"+str(team1overs)+"."+str(team1balls)+"\t"+str(team1runs)+"/"+str(team1wickets)+"\tOUT "+str(team1battingprobability[strike-1][bowler][0])+" BY "+str(team1battingprobability[strike-1][bowler][1])+"\n"
			strike = team1wickets+2
		elif(team1wickets<10):
			pos = 2
			for k in [2,4,6,8,10,12,14]:
				if(team1battingprobability[strike-1][bowler][k]>team1battingprobability[strike-1][bowler][pos]):
					pos = k
			maxprob = 0
			for k in [3,5,7,9,11,13,15]:
				if(team1battingprobability[strike-1][bowler][k]>team1battingprobability[strike-1][bowler][pos]):
					maxprob = k
			for k in [2,4,6,8,10,12,14]:
				if(k!=pos):
					team1battingprobability[strike-1][bowler][k]=team1battingprobability[strike-1][bowler][k]+team1battingprobability[strike-1][bowler][k+1]
			team1battingprobability[strike-1][bowler][pos]=team1battingprobability[strike-1][bowler][pos]-1
			perballplay = (pos-2)/2
			team1runs = team1runs + perballplay
			team1bowlingprobability[bowler][1] = team1bowlingprobability[bowler][1]+team1bowlingprobability[bowler][2]*2
			team1balls = team1balls+1
			print str(team1overs)+"."+str(team1balls)+"\tRuns: "+str(perballplay)+"\t"+str(team1battingprobability[strike-1][bowler][0])+"   Vs   "+str(team1battingprobability[strike-1][bowler][1])
			if(perballplay%2!=0):
				temp = strike
				strike = nonstrike
				nonstrike = temp
		if(team1wickets>9):
			break
	if(team1wickets>9):
		break
	team1overs = team1overs+1

print "FINAL SCORE:\t"+str(team1runs)+"/"+str(team1wickets)+"\tIN "+str(team1overs)+"."+str(team1balls)+"\tBY "+matchorder[6][2]

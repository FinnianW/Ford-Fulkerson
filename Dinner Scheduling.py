'''
Finnian Wengerd
Algorithms: Network Flow
Paper 2
Professor Daniel Showalter
Problem 15
04/10/2019

Given a set number of people (p) and days (d), where p == d, and sets of days(S)
where persons {p1,...,pn} are unavailable to cook dinner,
find a Bipartite Graph (G) that represents the perfect matching
if and only if there exists a feasible schedule

'''
from datetime import datetime
import random
#test case:

def start(p,d,S):
    p = p
    d = d
    S = S
    Available = {}
    allEdges = {}
    src = 'src'                 #initialize src
    sink = 'sink'               #initialize sink
    timeframeDict = {}          #initialize timeframe as a dictionary

            
    '''This function takes the days unavailable and
    creates a dict of available days for each person'''

    def createAvailable():
        global timeframe
        timeframe = ['d'+str(day) for day in range(1,d+1)]
        for person, days in S.items():
            x = str(days)
            x = x[1:-1]
            Available[person] = [possible for possible in timeframe if possible not in days]


    '''This function adds the src to the dictionary Available and the sink to the timeframeDict (see Lights and Switches start())'''
    def createSrcSink():
        Available[src] = []         #Adds the key src to the Available dictionary
        Available[sink] = []
        for person in Available:    #for each person including src listed in dictionary
            if person is not src and person is not sink:   #removes src as an option to iterate through
                Available[src].append(person)   #add person as a connection to src
        for days in timeframe:      #for each day listed in timeframe (for each day of the week)
            timeframeDict[days] = [sink] #add the key day and connect sink as the connection in timeframeDict
    '''
    This function first combines the dictionaries Available and timeframeDict to show all of the possible edges from src to sink.
    Then it lookes through the available edges and finds a path
    through the graph that allows each
    p to have one d and vice versa (See Lights and Switches tryPath())'''

    def tryPath():
        allEdges = {**Available, **timeframeDict}
        pointer = src                                                #pointer starts at the source
        visited = []                                                 #A list of visited nodes
        counter = 0                                                 #Starts the counter for times the pointer has been at sink
        while allEdges[pointer] != [] and pathExists(allEdges, pointer): #While the pointer has no children and a path from the
                                                                       #pointer to the sink still exists
            next_node = allEdges[pointer][0]                        #the next node is set to the first/left child
            
            allEdges[pointer].remove(next_node)                     #removes the path taken from parent to child from allEdges
            allEdges[next_node].append(pointer)                     #adds a new opposite edge from child to parent in allEdges
            if next_node not in visited:                            #if the child of the current node has not been visited
                visited.append(next_node)                           #go to the child and record the path in visited
                pointer = next_node
            else:
                visited.remove(next_node)                           #if not, remove the child from the visited list
                pointer = next_node
            if next_node == "sink":                                 #If the visited node is the sink
                counter +=1
                pointer = src
                
        if p == counter:                           #if there are the same number of edges leaving the src as there are entering the sink
            #print("True")                                           #There is a solution
            return True
        else:
            #print("False")                                          #There is no solution
            return False


    #This function checks to see if a path from a starting place to the sink still exists
    def pathExists(allEdges,start):
        examined = []
        queue = [start]
        while queue != []:
            pointer = queue.pop(0)
            examined.append(pointer)
            for child in allEdges[pointer]:
                if child == sink:
                    return True
                if child not in queue and child not in examined:
                    queue.append(child)
        return False
    createAvailable()
    createSrcSink()
    tryPath()
    endtime = datetime.now()
    return endtime
#Begin


p = 3200
d = 3200
S = {}
def testcase():
    S = {}
    for i in range(1,p+1):
        randomDayJ = random.randint(1,d)
        for j in range(randomDayJ):
            mynumday = 'd'+str(random.randint(1,d))
            if 'p'+str(i) not in S:  
                S['p'+str(i)] = [mynumday]
            else:
                if mynumday not in S['p'+str(i)]:
                    S['p'+str(i)].append(mynumday)

 
totalTime = []
deltaT = 0
totalseconds = 0
averageTime = 0


for i in range(1):
    testcase()
    starttime = datetime.now()
    endtime = start(p,d,S)
    deltaT = endtime-starttime
    totalTime.append(deltaT.total_seconds())
for i in totalTime:
    totalseconds +=i
averageTime = (totalseconds/len(totalTime))

print("Average runtime: %f seconds." %(averageTime))

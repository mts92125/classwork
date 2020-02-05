import numpy as np
import matplotlib.pyplot as p
# Naming for packages with the keyword as is not necessary
import csv

'''
Functions
'''
# The function is a template to save excel compatible csv files
def saveListToFile(wll, path): # Note we can give it another name to be used in the function 
    with open(path, 'a') as csvfile: # open file for writing
        writer = csv.writer(csvfile) # create a write variable
         
        writer.writerow(wll) # Use built-in writer function
    csvfile.close()  # CLOSE THE FILE  !!! Common error source
    
# the function learned from DLA5.py    
def runWalker():
    '''
    Local variables are only defined in the function itself
    '''
    walkerLength=0
    
    p.ion()
    #Select the starting position of the x-ax
    startX=np.random.randint(0,200)
    startAx=np.random.randint(0,4)
    #Set the starting position from where the random walker starts walking
    # NOTE Special case: for short statements we don't need to use idenetation if the whole program block fits within one line
    if startAx==0: startPos=np.array([0,startX])
    elif startAx==1: startPos=np.array([199,startX])
    # NOTE: Recognize that the syntax below with identation is eqally good than the syntax above if only one line is executed.
    elif startAx==2: 
        startPos=np.array([startX,0])
    elif startAx==3: 
        startPos=np.array([startX,199])
    
    # Walk as long no taken position is reached
    while a[startPos[0],startPos[1]] == 0:
        #NOTE: while loops, for loops and if define a program block. Every program block needs identation. 
        walkerLength+=1
        #Randomly choose a step to go
        step=np.array(stepChoices[np.random.randint(0,4)])
        #Add the step to the current position
        startPos=startPos+step
        # If the new position is within the array
        if startPos[0]>=0 and startPos[1]>=0 and startPos[0]<200 and startPos[1]<200:
            # If the current position is already taken we want to extend the structure
            if a[startPos[0],startPos[1]] > 0: # Remember we initialized our drawing array with zeros. 
                # Set the last position as taken aka stick to the structure. Here we set the value in the array to the distance from the center
                a[(startPos-np.array(step))[0],(startPos-np.array(step))[1]]=np.linalg.norm(np.array([(startPos-np.array(step))[0],(startPos-np.array(step))[1]])-np.array([100,100]),2)
                # refresh the image
                im.set_data(a) # set the data
                p.draw() # draw the image
                p.pause(0.001) # give the computer time to draw
        else:
            # else go 1 step back and choose again
            startPos=startPos-np.array(step)
        p.ioff()
    return walkerLength

'''
Global variables: can be accessed from anywhere
'''
# Array to walk in
a = np.zeros((200, 200))
#Possible increments of steps
stepChoices=[[-1,0],[0,-1],[1,0],[0,1]]

#Position to stick to initially
a[100,100]=1
startPos=[]
im = p.imshow(a, cmap='viridis')
walkerLengthList=[] #make a list
#We want 1000 walkers to stick to the structure
for t in range (0,20):
    
    a = np.zeros((200, 200))
#Possible increments of steps
    stepChoices=[[-1,0],[0,-1],[1,0],[0,1]]

#Position to stick to initially
    a[100,100]=1
    startPos=[]
    im = p.imshow(a, cmap='viridis')
    walkerLengthList=[] #make a list
#We want 1000 walkers to stick to the structure = np.zeros((200, 200))
#Possible increments of steps
 
    
    for i in range(0,1000): # some while loops can be turned into for loops
        print ("Walker running: "+str(i)) # Output on command line. Helpful for debugging to see if the loop is running
        walkerLength=runWalker()
        walkerLengthList.append(int(walkerLength))
        print ("Total Length: "+str(walkerLength))
 
#Saving file at a chosen location
    saveListToFile(walkerLengthList,'/Users/tindall_smith/Desktop/walkerList.csv')        

# make a figure of the size of the array
p.figure(2)
# show the array
p.imshow(a, cmap='viridis')
p.show()

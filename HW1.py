# Assignment: Cpts 315 HW 1 - A-Priori Algorithm
# Programmer: Rahul Singal (11471764)
# Date Created: 1/30/18
# Date Last Edited: 1/30/18
# Description: Use the A-Priori Algorithm to determine buying trends in an 
#              Amazon Dataset of Market Baskets
# Collaborators: Prof. Doppa in class pseduocode & slides


#Import Dataset
filename = open('browsingdata.txt', 'r')
dataset = filename.read().splitlines()
filename.close()

#Initialize a dict for keeping counts of unique items in basket
L1 = [] #Frequent items of size 1
L2 = [] #Frequent items of size 2
L3 = [] #Frequent items of size 3
C1 = {} #Candidates of Size 1
C2 = {} #Candidates of Size 2
C3 = {} #Candidates of Size 3

#Now take a subset of Dataset
practiceData = dataset[0:12]
#practiceData = dataset 

#************************ 1 **********************
#Looping through every line individually in practiceData
for line in practiceData:       
    #Go through the entire basket
    while (len(line) > 0):
        #Check to see if the first 8 characters is already in count dict    
        if (line[0:8]) in C1:            
            #Increment count
            C1[line[0:8]] = C1[line[0:8]] + 1 
        else:
            #Create new key and count to 1
            C1[line[0:8]] = 1         
        #Moves onto the next characters and disregards the space
        line = line[9:] 

#For an item in entire set
for key in C1:
    if C1[key] > 3: #Change to 100 for real data
        #Put into L1
        L1.append(key)
        
#Now take all the L1, and make every possible unique pair of size 2 in C2
i = 0
j = 0
for i in range (0, len(L1)):
    for j in range (i+1, len(L1)):
        #print(L1[i], L1[j])
        #Put each into C2 and make count 0 initially
        C2[L1[i], L1[j]] = 0

count = 0
i = 0
j = 0

#C2 now contains all unique pairs of size 2
"""for key in C2:
    for line in practiceData:
        for i in range (0, len(line))"""
#for line in practiceData:
    

#Then take each unique pairs and determine if both items exists in practiceData, 
#  put into C2 using same concept as 1
#Then check to see if the key in C2 is > 100. 
#Then take every unique pair in C2, and make C3 with all the L1 added to it
#Now check to see if all three items exists in practiceData
#Put into C3 using same 

    
        
    
      
        
        











#Make a dict that holds item key and count
dict1 = {}

#To set an element just do 
dict1['ELE17451'] = 1

#To increment do
dict1['ELE17451'] = dict1['ELE17451'] + 2








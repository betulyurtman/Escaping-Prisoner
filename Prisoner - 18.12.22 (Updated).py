#Importing the necessary libraries.
#Here numpy is for calculating the mean and variance.
#The random is for creating a random number for each simulation loop.
import numpy as np
import random as rd

#Here, we create an escape function for the simulation.
def escape(limit): 
    
    #The selection probabilities for each door.
    d1 = 0.1
    d2 = 0.2 
    d3 = 0.3 
    d4 = 0.1   
    d5 = 0.3
    
    #t is for counting the escape day. We start from 0.
    t = 0
    
    #This list is for saving the days i took while trying to get free for each simulation.
    days_to_freedom = []
    
    #N is for counting the simulations.
    N = 0
    
    #Creating a while loop to run while N is smaller than the limit we set.
    while N < limit:
        
        #Selecting a random number between 1 and 100 to select the door.
        r = rd.randint(1,100) 
        
        #Converting the selection probabilities for easy calculation.
        d1p = d1*100
        d2p = d2*100
        d3p = d3*100
        d4p = d4*100
        d5p = d5*100
        
        #Creating intervals for the doors.
        #When there is probablities given, we create intervals according to their probablities.
        
        #If the random number is between 1 and 10, 1.door is selected.
        if r >=1 and r <= d1p:
            
            t += 3 #We add 3 to t as it takes 3 days to go back to the cell without reaching to freedom.
            
        #If the random number is between 11 and 30, 2.door is selected.
        elif r >= d1p+1 and r <= d1p+d2p:
            
            t += 1 #We add 1 to t as it takes 1 days to go back to the cell without reaching to freedom.
            
        #If the random number is between 31 and 60, 3.door is selected.
        elif r >= d1p+d2p+1 and r <= d1p+d2p+d3p:
            
            t += 0 #This is not necessary but it could have been different than 0, so we add this too.
            
            #As the door 3 takes the prisoner to freedom, we save the days it took to reach the freedom to our list.
            #We reset t to 0 and add 1 to N.
            days_to_freedom.append(t)
            t = 0
            N += 1
            
        #If the random number is between 61 and 70, 4.door is selected.
        elif r >= d1p+d2p+d3p+1 and r <= d1p+d2p+d3p+d4p:
            
            t += 2 #We add 2 to t as it takes 2 days to reach the freedom.
            
            #As the door 3 takes the prisoner to freedom, we save the days it took to reach the freedom to our list.
            #We reset t to 0 and add 1 to N.
            days_to_freedom.append(t)
            t = 0
            N += 1
            
        #If the random number is between 71 and 100, 5.door is selected.
        elif r >= d1p+d2p+d3p+d4p+1 and r <= d1p+d2p+d3p+d4p+d5p:
            
            t += 4 #We add 4 to t as it takes 4 days to go to the cell without reaching to freedom.
            
    #We compute the variance and mean of the days it took to reach the freedom. 
    variance = round(np.var(days_to_freedom), 3)
    mean = np.mean(days_to_freedom)
    print("This is the mean:", mean)
    print("This is the variance:", variance)      

#Calling the function.
print("For 20 times:")
escape(20)
print("For 50 times:")
escape(50)
print("For 100 times:")
escape(100)
print("For 500 times:")
escape(500)
print("For 1000 times:")
escape(1000)
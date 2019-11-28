# Dataload function
import numpy as np
import pandas as pd
def dataLoad(filename):
    
    #Taget fra test projekt 1. 
    try: #Tjekker om filen kan findes og kan læses
        fil = pd.read_csv(filename) #Åbner og læser filen så den kan bruges
    except FileNotFoundError:
        return "Data file not found, please try again"  
    
    for i in range(np.size(np.array(fil.StudentID))):
        if i == 0:
            grades = np.array(fil.iloc[i,2:])
        else: 
            gradesi = np.array(fil.iloc[i,2:])
            grades = np.vstack((grades,gradesi))
    
    return grades
#print(dataLoad("DataArk1.csv"))











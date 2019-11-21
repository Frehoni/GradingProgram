# Dataload function
import numpy as np
import pandas as pd
from collections import Counter
def dataLoad(filename):
    #Taget fra test projekt 1. 
    try: #Tjekker om filen kan findes og kan læses
        fildata = pd.read_csv(filename) #Åbner og læser filen så den kan bruges
        print(fildata)
    except FileNotFoundError:
        return "Date file not found, please try again"
    studentid =np.array(fildata.StudentID)
    repeats = np.array([item for item, count in Counter(studentid).items() if count > 1]) #https://stackoverflow.com/a/11528581
    
    
    return (repeats)
print(dataLoad("DataArk1.csv"))
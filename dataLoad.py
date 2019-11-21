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
    studentid =np.array([filedata.StudentID])
    repeats = [item for item, count in Counter(studentid).iteritems() if count > 1]
    
    
    return (repeats)
print("")
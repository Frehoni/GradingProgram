# Dataload function
import numpy as np
import pandas as pd
def dataLoad(filename):
    #Taget fra test projekt 1. 
    try: #Tjekker om filen kan findes og kan læses
        grades = pd.read_csv(filename) #Åbner og læser filen så den kan bruges
        #print(fildata)
    except FileNotFoundError:
        return print("Date file not found, please try again")    
    
    return grades
print(dataLoad("DataArk1.csv"))











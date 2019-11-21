# Dataload function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
def dataLoad(filename):
    grades = np.array([])
    numbers = np.array([])
    assignments = np.array(['StudentID','Name'])
    #Taget fra test projekt 1. 
    try: #Tjekker om filen kan findes og kan læses
        fildata = pd.read_csv(filename) #Åbner og læser filen så den kan bruges
        #print(fildata)
    except FileNotFoundError:
        return print("Date file not found, please try again")
    data = np.array(fildata)
    studentid =np.array(fildata.StudentID)
    repeats = np.array([item for item, count in Counter(studentid).items() if count > 1]) #https://stackoverflow.com/a/11528581
    for a in range(np.size(repeats)):
        print("The StudentID {} is stated more than once in the datafile.".format(repeats[a]))
    for b in range(np.size(studentid)):
        grade = np.array(fildata.iloc[b,2:])
        grades = np.append(grades,(np.sum(grade)/np.size(grade))) #np.mean gav os ingen decimaler, så vi gjorde det som en flok hulemennesker ville.
    for c in range(np.size(fildata.iloc[0,:])-2):
        assignments = np.append(assignments,'Assignment {}'.format(c+1))
    numbers = np.arange(1,np.size(studentid)+1)
    assignments = np.append(assignments,'Average Grade')
    finaldata = np.c_[data,grades]
    df = pd.DataFrame(finaldata,columns=assignments,index=numbers)
    df_sort = df.sort_values('Name')
    print(df,df_sort)
    
    return (grades)
print(dataLoad("DataArk1.csv"))
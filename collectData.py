#Error handling

import numpy as np
import pandas as pd
from collections import Counter
def collectData(grades,finalgrades):
    assignments = np.array(['StudentID','Name'])
    data = np.array(grades)
    studentid =np.array(grades.StudentID)
    repeats = np.array([item for item, count in Counter(studentid).items() if count > 1]) #https://stackoverflow.com/a/11528581
    for a in range(np.size(repeats)):
        print("The StudentID {} is stated more than once in the datafile.".format(repeats[a]))

       
    for c in range(np.size(grades.iloc[0,:])-2):
        assignments = np.append(assignments,'Assignment {}'.format(c+1))
    numbers = np.arange(1,np.size(studentid)+1)
    assignments = np.append(assignments,'Average Grade')
    finaldata = np.c_[data,finalgrades]
    df = pd.DataFrame(finaldata,columns=assignments,index=numbers)
    df_sort = df.sort_values('Name')
    print(grades)
    print(df_sort)
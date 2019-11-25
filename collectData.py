#Error handling

import numpy as np
import pandas as pd
from collections import Counter
def collectData(filename,finalgrades):
    fil = pd.read_csv(filename)
    assignments = np.array(['StudentID','Name'])
    data = np.array(fil)
    studentid =np.array(fil.StudentID)
    #Er I mainscript istedet
    #repeats = np.array([item for item, count in Counter(studentid).items() if count > 1]) #https://stackoverflow.com/a/11528581
    #for a in range(np.size(repeats)):
        #print("The StudentID {} is stated more than once in the datafile.".format(repeats[a]))

       
    for c in range(np.size(fil.iloc[0,:])-2):
        assignments = np.append(assignments,'Assignment {}'.format(c+1))
    numbers = np.arange(1,np.size(studentid)+1)
    assignments = np.append(assignments,'Average Grade')
    finaldata = np.c_[data,finalgrades]
    df = pd.DataFrame(finaldata,columns=assignments,index=numbers)
    df_sort = df.sort_values('Name')
    print("Original data:")
    print(fil)
    print("Sorted data:")
    print(df_sort)
    
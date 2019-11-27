#Error handling

import numpy as np
import pandas as pd
    
def collectData(filename,finalgrades):
    fil = pd.read_csv(filename)
    assignments = np.array(['StudentID','Name'])
    data = np.array(fil)
    studentid =np.array(fil.StudentID)
       
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
    with pd.option_context('display.max_rows', None, 'display.max_columns', None): #https://stackoverflow.com/a/30691921
        print(df_sort)
    
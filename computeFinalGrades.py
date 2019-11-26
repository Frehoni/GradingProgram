# Final grade function
import pandas as pd
import numpy as np
def computeFinalGrades(grades):
    grades1 = np.array([])
    #data = np.array(grades)
    #studentid = np.array(grades.StudentID)
    for b in range(grades.shape[0]):#Calculating Average
        if -3 in grades[b,:]:#Failing the student
            grades1 = np.append(grades1,-3)
        else:
            if np.size(grades[b,:]) == 1:
                grades1 = np.append(grades1,grades[b,:])
            if np.size(grades[b,:]) > 1:
                grade = grades[b,:]
                grade = np.delete(grade,grade.argmin())
                grades1 = np.append(grades1,(np.sum(grade)/np.size(grade))) #np.mean gav os ingen decimaler, så vi gjorde det som en flok hulemennesker ville.
            if np.size(grades[b,:]) == 0:
                print("There are no grades!")
    grades = grades1
    gradesFinal = roundGrade(grades)
    
    return gradesFinal
#print(computeFinalGrades(np.array(([7,-3,10],[2,4,7],[4,7,10],[12,12,12],[2,2,2],[10,10,10]))))
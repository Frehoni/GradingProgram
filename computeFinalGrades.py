# Final grade function
import pandas as pd
import numpy as np
def computeFinalGrades(grades):
    grades1 = np.array([])
    data = np.array(grades)
    studentid = np.array(grades.StudentID)
    for b in range(np.size(studentid)):#Calculating Average
        if -3 in np.array(grades.iloc[b,2:]):
            grades1 = np.append(grades1,-3)
        else:
            if np.size(np.array(grades.iloc[b,2:])) == 1:
                grades1 = np.append(grades1,grades.iloc[b,2:])
            if np.size(np.array(grades.iloc[b,2:])) > 1:
                grade = np.array(grades.iloc[b,2:])
                grade = np.delete(grade,grade.argmin())
                grades1 = np.append(grades1,(np.sum(grade)/np.size(grade))) #np.mean gav os ingen decimaler, så vi gjorde det som en flok hulemennesker ville.
            if np.size(np.array(grades.iloc[b,2:])) == 0:
                print("There are no grades!")
    grades = grades1
    gradesFinal = roundGrade(grades)
    
    return gradesFinal
print(computeFinalGrades(pd.read_csv("DataArk1.csv")))
# Grade Rounding function
import numpy as np


def roundGrade(grades):
    posgrades = np.array([-3,0,2,4,7,10,12]) #Possible roundable grades
    middlenr = np.array([-1.5,1,3,5.5,8.5,11]) #Numbers to round up
    gradesRounded = np.array([]) #Placeholder
    for l in range(np.size(grades)): #Finds numbers to round up and numbers to remove. 
        if grades[l] in middlenr:
            grades[l] = grades[l]+1 #Ensures that the round-up function is working correctly. 
        if grades[l] < (-3) or grades[l] > 12:
            print("Error at grade nr. {}. Grade is not in accepted range and has been removed.".format(l+1))
    grades = grades[grades<=12]
    grades = grades[grades>=-3]
    for i in range(np.size(grades)): #Finds the nearest number and rounds it to the closets value in posgrades array.
        rg = min(posgrades, key=lambda x:abs(x-grades[i])) #https://stackoverflow.com/a/12141207
        gradesRounded = np.append(gradesRounded,rg)
        
    return gradesRounded

print(roundGrade(np.array([-4,5,8.5,3,12,15,6,-1.5,1,3,5.5,8.5,11])))

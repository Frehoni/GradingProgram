# Main script
import pandas as pd
import numpy as np
from collections import Counter
#Taget fra test projekt 1.
istheredata = False #Tjek for data. Taget fra test projekt 1.
array = np.array([]) 
#Define menu items
menuItems =np.array(["Load new data","Check for data errors","Generate plots.","Display list of grades","Quit"])
posgrades = np.array([-3,0,2,4,7,10,12])
while True:
    #Display menu
    choice = displayMenu(menuItems)
    
    #Load new data#
    if choice ==1:
        while True:
            filename = input("Please enter the full file name, for example \"file.csv\" : ")
            if type(dataLoad(filename)) == type(array):
                istheredata = True
                grades = dataLoad(filename)
                gradesFinal = computeFinalGrades(grades)
                break
            else:
                istheredate = False
                print(dataLoad(filename))



    #Check for data errors
    elif choice == 2:

    
        if istheredata != True:
            while True:
                print("Missing datafile. Please insert a file before this function can run:")
                filename = input("Please enter the full file name, for example \"file.csv\" : ")
                if type(dataLoad(filename)) == type(array):
                    istheredata = True
                    grades = dataLoad(filename)
                    gradesFinal = computeFinalGrades(grades)
                    break
                else:
                    istheredate = False
                    print(dataLoad(filename))
        erroroptions = np.array(['Check for dublicate StudentIDs','Check for invalid grades','Check for all mentioned errors','Go back'])
        while True:
            errorchoice = displayMenu(erroroptions)
            fil = pd.read_csv(filename)
        
            #Checking for dublicate student ID's
            if errorchoice == 1:
                studentid = np.array(fil.StudentID)
                repeats = np.array([item for item, count in Counter(studentid).items() if count > 1]) #https://stackoverflow.com/a/11528581
                for a in range(np.size(repeats)):
                    print("The StudentID {} is stated more than once in the datafile.".format(repeats[a]))
            
            #Checking for invalid grades
            elif errorchoice == 2:
                for l in range(fil.shape[0]): #Finds numbers that aren't valid.
                    check = np.array(fil.iloc[l,2:])
                    for checksize in range(np.size(check)):
                        if check[checksize] not in posgrades:
                            print("Error at row nr. {} with grade(s): {}. Grade {} is not in accepted range.".format(l+1,check,check[checksize]))
            
            #Checking for everything
            elif errorchoice == 3:
                studentid = np.array(fil.StudentID)
                repeats = np.array([item for item, count in Counter(studentid).items() if count > 1]) #https://stackoverflow.com/a/11528581
                for a in range(np.size(repeats)):
                    print("The StudentID {} is stated more than once in the datafile.".format(repeats[a]))            
                for l in range(fil.shape[0]): #Finds numbers that aren't valid.
                    check = np.array(fil.iloc[l,2:])
                    for checksize in range(np.size(check)):
                        if check[checksize] not in posgrades:
                            print("Error at row nr. {} with grade(s): {}. Grade {} is not in accepted range.".format(l+1,check,check[checksize]))
            elif errorchoice ==4:
                break
            
            
            
            
            
    
    
    
    #Generate plots
    elif choice == 3:
        if istheredata != True:
            while True:
                print("Missing datafile. Please insert a file before this function can run:")
                filename = input("Please enter the full file name, for example \"file.csv\" : ")
                if type(dataLoad(filename)) == type(array):
                    istheredata = True
                    grades = dataLoad(filename)
                    gradesFinal = computeFinalGrades(grades)
                    break
                else:
                    istheredate = False
                    print(dataLoad(filename))        
        print(gradesPlot(grades,gradesFinal))

   
    
    
    #Display list of grades
    elif choice ==4:
        if istheredata != True:
            while True:
                print("Missing datafile. Please insert a file before this function can run:")
                filename = input("Please enter the full file name, for example \"file.csv\" : ")
                if type(dataLoad(filename)) == type(array):
                    istheredata = True
                    grades = dataLoad(filename)
                    gradesFinal = computeFinalGrades(grades)
                    break
                else:
                    istheredate = False
                    print(dataLoad(filename))       
            
        print(collectData(filename,gradesFinal))
                
        
    
    #Quit
    elif choice ==5:
        break
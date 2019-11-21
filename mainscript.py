# Main script
import pandas as pd
import numpy as np
#Taget fra test projekt 1.
istheredata = False #Tjek for data. Taget fra test projekt 1.
array = np.array([]) 
#Define menu items
menuItems =np.array(["Load new data","Check for data errors","Generate plots.","Display list of grades","Quit"])

while True:
    #Display menu
    choice = displayMenu(menuItems);
    
    #Load new data#
    if choice ==1:
        filename = input("Please enter the full file name, for example \"file.csv\" : ")
        grades = dataLoad(filename)
        if type(grades) == type(array): #Check if the data was approved 
            istheredata = True
        else:
            istheredate = False
        gradesFinal = computeFinalGrades(grades)
        print(gradesFinal,grades)
    #Check for data errors
    elif choice == 2:

    
        if istheredata != True:
            print("Missing datafile. Please insert a file before this function can run:")
            filename = input("Please enter the full file name, for example \"file.csv\" : ")
            grades = dataLoad(filename)
            if type(grades) == type(array):
                istheredata = True
            else:
                istheredate = False
                pass
        
    
    
    
    
    
    #Generate plots
    elif choice == 3:
        if istheredata != True:
            print("Missing datafile. Please insert a file before this function can run:")
            filename = input("Please enter the full file name, for example \"file.csv\" : ")
            grades = dataLoad(filename)
            if type(grades) == type(array):
                istheredata = True
            else:
                istheredate = False
                pass  
        pass

    #Display list of grades
    elif choice ==4:
        if istheredata != True:
            print("Missing datafile. Please insert a file before this function can run:")
            filename = input("Please enter the full file name, for example \"file.csv\" : ")
            grades = dataLoad(filename)
            if type(grades) == type(array):
                istheredata = True
            else:
                istheredate = False
                pass          
        
        
        pass
    
    #Quit
    elif choice ==5:
        break
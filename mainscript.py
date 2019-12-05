#The code has been writen equally between both groupmembers.
# Main script
import pandas as pd
import numpy as np
from collections import Counter
#Taget fra test projekt 1.
istheredata = False #Tjek for data. Taget fra test projekt 1.
array = np.array([]) 
#Define menu items
menuItems =np.array(["Load new data","Check for data errors","Generate plots.","Display list of grades","Quit"]) #MenuOptions
fileitems = np.array(["Insert CSV-file","Go back"]) #Menu options for filereading
posgrades = np.array([-3,0,2,4,7,10,12]) #The possible grades
while True:
    #Display menu
    choice = displayMenu(menuItems)
    
    #Load new data#
    if choice ==1:
        while True: #Loads data
            
            filechoice = displayMenu(fileitems)
            if filechoice == 1:
                filename = input("Please enter the full file name, for example \"file.csv\" : ") #Prompts the user to type a filename
                if type(dataLoad(filename)) == type(array): #If the datafile is invalid, a string is returned. If it's an array, the data was accepted.
                    
                    grades = dataLoad(filename) #Saves the unsorted grades as a variable
                    gradesFinal = computeFinalGrades(grades) #Saves the final sorted grades as a variable
                    if type(gradesFinal) == type("string"): #If the data is invalid, the loop continues and an error message is printed
                        print(gradesFinal)
                    else:
                        istheredata = True
                        break
                else: #If the grades are not a vector, then the loop continues. 
                    istheredate = False
                    print(dataLoad(filename))
            elif filechoice ==2: #Exits the loop to type in a datafile. 
                break



    #Check for data errors
    elif choice == 2:

    
        if istheredata != True: #Checks if there's any valid data, and if not, prompts the user to load the data.
            while True: #From here, the code is the same as in the data load function
                print("Missing datafile. Please insert a file before this function can run:")
                filechoice = displayMenu(fileitems)
                if filechoice == 1:
                    filename = input("Please enter the full file name, for example \"file.csv\" : ")
                    if type(dataLoad(filename)) == type(array):
                        grades = dataLoad(filename)
                        gradesFinal = computeFinalGrades(grades)
                        if type(gradesFinal) == type("string"):
                            print(gradesFinal)
                            pass
                        else:
                            istheredata = True
                            break                            
                    else:
                        istheredate = False
                        print(dataLoad(filename))
                elif filechoice ==2:
                    break
        elif istheredata == True: #If the data is now valid, the function can run. 
            #The menu options
            erroroptions = np.array(['Check for dublicate StudentIDs','Check for invalid grades','Check for all mentioned errors','Go back'])
            while True:
                errorchoice = displayMenu(erroroptions)
                fil = pd.read_csv(filename)
            
                #Checking for dublicate student ID's
                if errorchoice == 1:
                    studentid = np.array(fil.StudentID)#Makes an array with the studentIDs
                    #Makes an array with the studentIDs that are mentioned more than once.
                    repeats = np.array([item for item, count in Counter(studentid).items() if count > 1]) #https://stackoverflow.com/a/11528581
                    for a in range(np.size(repeats)):
                        print("The StudentID {} is stated more than once in the datafile.".format(repeats[a])) #Prints an error with the dublicate students
                
                #Checking for invalid grades
                elif errorchoice == 2 :
                    for l in range(fil.shape[0]): #Finds numbers that aren't valid.
                        check = np.array(fil.iloc[l,2:]) #Loops through the different grades for each student
                        for checksize in range(np.size(check)): #Takes and chekcs each grade in each life
                            if check[checksize] not in posgrades: #Checks if the grade is an accepted possible grade
                                print("Error at row nr. {} with grade(s): {}. Grade {} is not in accepted range.".format(l+1,check,check[checksize])) #Prints an error with the invalid grades.
    
                #Checking for all errors:
                elif errorchoice ==3: #Does what option 1 and 2 does at the same time.
                    studentid = np.array(fil.StudentID)
                    repeats = np.array([item for item, count in Counter(studentid).items() if count > 1]) #https://stackoverflow.com/a/11528581
                    for a in range(np.size(repeats)):
                        print("The StudentID {} is stated more than once in the datafile.".format(repeats[a]))
                    for l in range(fil.shape[0]): #Finds numbers that aren't valid.
                        check = np.array(fil.iloc[l,2:])
                        for checksize in range(np.size(check)):
                            if check[checksize] not in posgrades:
                                print("Error at row nr. {} with grade(s): {}. Grade {} is not in accepted range.".format(l+1,check,check[checksize]))
                
                
                
                #Go back
                elif errorchoice ==4: 
                    break                          

               
    #Generate plots
    elif choice == 3:
        if istheredata != True:#Checks if there's valid data
            while True:#Does the same as in the load data function
                print("Missing datafile. Please insert a file before this function can run:")
                filechoice = displayMenu(fileitems)
                if filechoice == 1:
                    filename = input("Please enter the full file name, for example \"file.csv\" : ")
                    if type(dataLoad(filename)) == type(array):
                        grades = dataLoad(filename)
                        gradesFinal = computeFinalGrades(grades)
                        if type(gradesFinal) == type("string"):
                            print(gradesFinal)
                        else:
                            istheredata = True
                            break
                    else:
                        istheredate = False
                        print(dataLoad(filename))
                elif filechoice ==2:
                    break        
        elif istheredata == True: #Data is valid, the function then prints the plots via the plotfunction
            print(gradesPlot(grades,gradesFinal))                

   
    
    
    #Display list of grades
    elif choice ==4:
        if istheredata != True: #Checks if there's valid data
            while True: #Does the same as in the load data function
                print("Missing datafile. Please insert a file before this function can run:")
                filechoice = displayMenu(fileitems)
                if filechoice == 1:
                    filename = input("Please enter the full file name, for example \"file.csv\" : ")
                    if type(dataLoad(filename)) == type(array):
                        grades = dataLoad(filename)
                        gradesFinal = computeFinalGrades(grades)
                        if type(gradesFinal) == type("string"):
                            print(gradesFinal)
                        else:
                            istheredata = True
                            break
                    else:
                        istheredate = False
                        print(dataLoad(filename))
                elif filechoice ==2:
                    break     
        elif istheredata ==True: #Data is valid, the function then prints the list of grades via the collectData function
            print(collectData(filename,gradesFinal))
        
                
        
    
    #Quit
    elif choice ==5:
        break
#The code has been writen equally between both groupmembers.
# Grades plot
import numpy as np
import matplotlib.pyplot as plt

def gradesPlot(grades,gradesFinal):
    posgrades = np.array([-3,0,2,4,7,10,12])
    posgrades_string = ['-3','0','2','4','7','10','12']
    grades_zero = np.zeros(np.size(posgrades))
    for i in range(np.size(gradesFinal)):
        for k in range(np.size(posgrades)):
            if gradesFinal[i] == posgrades[k]:
                grades_zero[k] = grades_zero[k]+1
            else: 
                pass
        grade_there=grades_zero
    plt.figure(figsize=(12,8))
    y_akse = np.arange(np.max(grade_there)+1)
    plt.bar(posgrades_string,grade_there,color=['black','gray','red','orange','yellow','limegreen','green'])
    #https://stackoverflow.com/a/17574813
    plt.yticks(y_akse,y_akse)
    plt.title("Final Grades Barplot")
    plt.ylabel("Number of grades")
    plt.xlabel("Grades")
    plt.show()
    mean = np.array([])
    assignmentnr = np.array([])
    samletkarakter = np.array([])
    for a in range(grades.shape[1]):
        samletkarakter = np.append(samletkarakter,grades[:,a])
        mean = np.append(mean,np.mean(grades[:,a]))
        placeholder = np.ones(grades.shape[0])
        placeholder = placeholder + (a)
        assignmentnr = np.append(assignmentnr,placeholder)
    #https://matplotlib.org/tutorials/introductory/pyplot.html
    tillægx = np.random.uniform(-0.1,0.1,np.size(assignmentnr))
    tillægy = np.random.uniform(-0.1,0.1,np.size(assignmentnr))
    assignmentnrx = assignmentnr+tillægx
    samletkaraktery = samletkarakter+tillægy
    assignments = np.array([])
    for c in range(grades.shape[1]):
        assignments = np.append(assignments,'Assignment {}'.format(c+1))
    plt.figure(figsize=(12,8))
    plt.scatter(assignmentnrx,samletkaraktery,label="Grade distribution")
    plt.plot(np.arange(np.size(assignments))+1,mean,color='red',label="Grade average")
    plt.title("Scatter Plot")
    plt.yticks(posgrades,posgrades)
    plt.xticks(np.arange(np.size(assignments))+1)
    plt.ylabel("Grades")
    plt.xlabel("Assignment Number:")
    plt.legend(loc=0) #https://kite.com/python/examples/1880/matplotlib-add-a-figure-legend-at-the-%22best%22-position
    plt.grid(True)
    plt.show()
    
    
    
    
    
    
    
    
#print(gradesPlot(np.array(([2,10,12],[4,7,-3])),np.array([4,7,10,2,0,-3,12,10,4])))
            
        
            
                
                
            
            
            
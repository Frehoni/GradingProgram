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
    plt.yticks(y_akse,y_akse)
    plt.title("Final Grades Barplot")
    plt.ylabel("Number of grades")
    plt.xlabel("Grades")
    plt.show()
    
    assignmentnr = np.array([])
    samletkarakter = np.array([])
    for a in range(grades.shape[1]):
        samletkarakter = np.append(samletkarakter,grades[:,a])
        placeholder = np.ones(grades.shape[0])
        placeholder = placeholder + (a+1)
        assignmentnr = np.append(assignmentnr,placeholder)
    
    tillægx = np.random.randn(-0.1,0.1,np.size(assignmentnr))
    tillægy = np.random.randn(-0.1,0.1,np.size(assignmentnr))
    assignmentnrx = assignmentnr+tillægx
    samletkaraktery = samletkarakter+tillægy
    assignments = np.array([])
    for c in range(grades.shape[1]):
        assignments = np.append(assignments,'Assignment {}'.format(c+1))
        print(assignments)
    plt.scatter(assignmentnrx,samletkaraktery)
    plt.xlim(-3,12)
    plt.show()
    
    
    
    
    
    
    
    
print(gradesPlot(np.array(([1,2,3],[1,2,3])),np.array([4,7,10,2,0,-3,12,10,4])))
            
        
            
                
                
            
            
            
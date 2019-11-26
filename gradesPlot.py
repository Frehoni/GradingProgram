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
    plt.figure(figsize=(15,8))
    y_akse = np.arange(np.max(grade_there)+1)
    plt.bar(posgrades_string,grade_there,color=['black','gray','red','orange','yellow','limegreen','green'])
    plt.yticks(y_akse,y_akse)
    plt.title("Final Grades Barplot")
    plt.ylabel("Number of grades")
    plt.xlabel("Grades")
    plt.show()
    
print(gradesPlot(1,np.array([4,7,10,2,0,-3,12,10,4])))
            
        
            
                
                
            
            
            
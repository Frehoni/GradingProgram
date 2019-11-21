# Main script

import numpy as np

#Define menu items
menuItems =np.array(["Load new data","Check for data errors","Generate plots.","Display list of grades","Quit"])

while True:
    #Display menu
    choice = displayMenu(menuItems);
    
    # Enter name
    if choice ==1:
        name = input("Please enter your name: ")
    
    # Display greeting
    elif choice == 2:
        print(name)
    
    elif choice == 3:
        pass
    
    
    elif choice ==4:
        pass
    
    #Quit
    elif choice ==5:
        break
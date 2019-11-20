# Main script

import numpy as np

#Define menu items
menuItems =np.array(["Enter name","Display greeting","Quit"])

while True:
    #Display menu
    choice = displayMenu(menuItems);
    
    # Enter name
    if choice ==1:
        name = input("Please enter your name: ")
    
    # Display greeting
    elif choice == 2:
        print(name)
    
    #Quit
    elif choice ==3:
        break
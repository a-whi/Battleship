"""
Created by: Alex Whitfield
Battle ship main file

Rules I am following:
- Boats:
    - 1 x 5 size boat
    - 1 x 4 size boat
    - 2 x 3 size boat
    - 1 x 1 size boat
- Boats can be placed anywhere on boat, even next to each other

Method:
- We will use a probablility map, one will be created for all boats, then will be added
  together. 
- As we fire the maps will be updated
- When a ship is sunk we record what type of ship it is so we dont have to look for it.

"""

# Global values
grid_size = 10
hitTarget = [] # This will record grid positions for where we have hit a target
boatmap = []

##################################################################################################
def main():

    # Create tracking grid
    trackingGrid_creation()

    # Create ship probability map
    probMap()       #Work on the grid so it can update and work for all boat sizes

    if len(hitTarget) != 0:
        # If the list isn't empty it means last shot we hit a boat and need to search for it
        # Check up, down, left right 
        print()
    else:
        print(2,1)
        # Find highest probability and say it

##################################################################################################
# All to do with the probability map
def function_h(i, j, boat_length):
    z = 0
    while z < boat_length:
        boatmap[i][j+z] += 1
        z+=1
    
def function_v(i, j, boat_length):
    z = 0
    while z < boat_length:
        boatmap[i+z][j] += 1
        z+=1
# Create a probabilty map for each boat
def probMap():
    boat_length = 5
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            row.append(0)

        boatmap.append(row)

    for i in range(grid_size):   
        for j in range(grid_size):
            if j+boat_length <= grid_size:
                function_h(i, j, boat_length)
                
                if i+boat_length <= grid_size:
                    function_v(i, j, boat_length)
                    
            elif i+boat_length <= grid_size:
                function_v(i, j, boat_length)
                
                if j+boat_length <= grid_size:
                    function_h(i, j, boat_length)
            else:
                continue
    print(boatmap)
##################################################################################################

# This is a grid where every element is True or False, keeps track of where we have fired
def trackingGrid_creation(grid_size):
    trackingGrid = []
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            row.append(False)

        trackingGrid.append(row)

main()



####
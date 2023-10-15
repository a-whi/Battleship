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
boatType = [5,4,3,3,1]

##################################################################################################
def main():

    # Create tracking grid
    trackingGrid = trackingGrid_creation()

    # Create ship probability map
    probMap()

#Loop (While )
    # Find largest value in grid
    # Update trackingGrid
    # Say its location
    # If hit...
        # Loop (till boat destroyed)
            # Look destroy boat
        # Figure out how long the boat was
        # Remove from boat type
        # Recalculate new prob map
    # Else (miss), recalulate and do it again
##
    while len(boatType) != 0:
        x_cord, y_cord = largestNumber()
        trackingGrid[x_cord][y_cord] = True

        print(x_cord, y_cord)
        print()
        print("Hit or miss, Y or N?")
        feedback = input().lower()

        if feedback == 'y':
            hitTarget.append(x_cord,y_cord) 
            destroy_boat()  # Destroy boat function
        else:
            print()

##################################################################################################
# How will we find the rest of the boat, what happens if we hit the middle of the boatt
def destroy_boat():
    print()

##################################################################################################
# Finds largest number in the boatmap grid (Most likely spot for a boat to be)
def largestNumber():
    max_num = boatmap[0][0]
    row_index = 0
    col_index = 0

    for i, row in enumerate(boatmap):
        for j, number in enumerate(row):
            if number > max_num:
                max_num = number
                row_index = i
                col_index = j

    return row_index, col_index
    
##################################################################################################
# All to do with the probability map
# Could also be made cleaner
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

## Needs to be recalculated when we miss a target though + need to find the easiest way to find the max value on the map

# Create a probabilty map for where the most likely spot a boat could be
# Creates blank grid
def probMap():
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            row.append(0)

        boatmap.append(row)

# Time complexity is kinda high here
    # Loops through the list of boat sizes to be added on the probability map
    for x in range(len(boatType)):      # Feel this line could be better, currently works though
        boat_length = boatType[x]
        for i in range(grid_size):   
            for j in range(grid_size):
                # Figures out whether the boat can fit on the map
                if j+boat_length <= grid_size:
                    function_h(i, j, boat_length)   # Adds values for if the boat can fit horizontally
                    
                    if i+boat_length <= grid_size:
                        function_v(i, j, boat_length)   # Adds values for if the boat can fit vertically
                        
                elif i+boat_length <= grid_size:
                    function_v(i, j, boat_length)
                    
                    if j+boat_length <= grid_size:
                        function_h(i, j, boat_length)
                else:
                    continue

##################################################################################################

# This is a grid where every element is True or False, keeps track of where we have fired
def trackingGrid_creation():
    trackingGrid = []
    # This could be made better I think, since i & j are not used
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            row.append(False)

        trackingGrid.append(row)
    return trackingGrid

main()
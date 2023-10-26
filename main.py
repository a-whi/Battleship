"""
Created by: Alex Whitfield
Battle ship

Rules I am following:
- Boats:
    - 1 x 5 size boat
    - 1 x 4 size boat
    - 2 x 3 size boat
    - 1 x 2 size boat
- Boats can be placed anywhere on boat, even next to each other

Method:
- We will use a probablility map, one will be created for all boats, then will be added
  together. 
- As we fire the maps will be updated
- When a ship is sunk we record what type of ship it is so we dont have to look for it.

"""

# Global values
grid_size = 10
boatmap = []
boatType = [5,4,3,3,2]
trackingGrid = []

##################################################################################################
def main():
    # Create tracking grid
    trackingGrid_creation()

    # Create ship probability map
    probMap()
    hitTarget = []

    #Loop (While)
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
    #

    while len(boatType) != 0:
        x_cord, y_cord = largestNumber()
        trackingGrid[x_cord][y_cord] = True

        print('(',x_cord,',',y_cord,')')
        print("Hit or miss, H or M?")
        feedback = input().lower()

        if feedback == 'h':
            hitTarget.append((x_cord,y_cord)) 

            boatLen = destroy_boat(hitTarget)  # Destroy boat function + finds the length of the boat destroyed

            # Remove boat size from boatType list
            for i in range(len(boatType)):
                if boatType[i] == boatLen:
                    boatType.pop(i)
                    break
            hitTarget = []      # Should reset the list back to blank

            # Recalculate
            probMap()
###
        elif feedback == 'boat':
            print(boatmap)
###
        else:
            # Recalculate
            probMap()

    print('VICTORY, I crushed you')

##################################################################################################
def destroy_boat(hitTarget):
    # While ship not destroyed
        # Find highest value for adjacent coords
        # if left or right then its horizontal
        # if not horizontal, its vertical
        # Loop till eith destroyed ship or miss
            # If another hit, keep going in that direction +1 to hit_count 
            # If miss, go opposite way from hitTarget coord

    hit_count = 1   # Help us figure out the length of the boat
    destroyed = False   

    while destroyed == False:

        coord, direction = compareValues(hitTarget)
        print(coord) # Finds the best option out of the adjacent coords

        print("Hit or miss, H or M?")
        feedback = input().lower()

        if feedback == 'h':
            hit_count += 1

            print("Is ship destroyed? Y or N")
            feedback = input().lower()
            if feedback == 'y':
                destroyed = True
                break

            else:
                x = 1
                feedback1 = 'h'
                if direction == 1:
                    # WHILE target is hit, keep going in that direction and check if ship is destroyed
                    # once that breaks other while loop until ship is destroyed in opposite direction
                    while feedback1 == 'h':
                        if trackingGrid[coord[0]+x][coord[1]] == False:
                            trackingGrid[coord[0]+x][coord[1]] = True
                            print('(',coord[0]+x,',', coord[1],')')
                            print("Hit or miss, H or M?")
                            feedback1 = input().lower()

                            if feedback1 == 'h':
                                hit_count += 1

                                print("Is ship destroyed? Y or N")
                                feedback = input().lower()
                                if feedback == 'y':
                                    destroyed = True
                                    feedback1 = 'm' #Should break out of loop
                                    break
                                else: 
                                    continue
                    ###
                            elif feedback1 == 'boat':
                                print(boatmap)
                    ###
                        x += 1

                    x = 2
                    while destroyed == False:
                        if trackingGrid[coord[0]-x][coord[1]] == False:
                            trackingGrid[coord[0]-x][coord[1]] = True
                            print('(',coord[0]-x,',', coord[1],')')
                            print("Hit or miss, H or M?")
                            feedback = input().lower()
                            if feedback == 'h':
                                hit_count += 1

                                print("Is ship destroyed? Y or N")
                                feedback = input().lower()
                                if feedback == 'y':
                                    destroyed = True
                                    break
                                else: 
                                    continue
                    ###
                            elif feedback == 'boat':
                                print(boatmap)
                    ###
                            else:
                                print('ERROR, idk what happened but nowhere to hit ship')
                        x += 1

                else:
                    while feedback1 == 'h':
                        if trackingGrid[coord[0]][coord[1]+x] == False:
                            trackingGrid[coord[0]][coord[1]+x]= True
                            print('(',coord[0],',', coord[1]+x,')')
                            print("Hit or miss, H or M?")
                            feedback1 = input().lower()

                            if feedback1 == 'h':
                                hit_count += 1

                                print("Is ship destroyed? Y or N")
                                feedback = input().lower()
                                if feedback == 'y':
                                    destroyed = True
                                    feedback1 = 'm' #Should break out of loop
                                    break
                                else: 
                                    continue
                    ###
                            elif feedback == 'boat':
                                print(boatmap)
                    ###
                        x += 1

                    x = 2
                    while destroyed == False:
                        if trackingGrid[coord[0]][coord[1]-x] == False:
                            trackingGrid[coord[0]][coord[1]-x] = True
                            print('(',coord[0],',', coord[1]-x,')')
                            print("Hit or miss, H or M?")
                            feedback = input().lower()
                            if feedback == 'h':
                                hit_count += 1

                                print("Is ship destroyed? Y or N")
                                feedback = input().lower()
                                if feedback == 'y':
                                    destroyed = True
                                    break
                                else: 
                                    continue
                            else:
                                # Just so I know theres been a problem, but not really needed
                                print('ERROR, idk what happened but nowhere to hit ship') 
                ###
                        elif feedback == 'boat':
                            print(boatmap)
                ###
                        x += 1

###
        elif feedback == 'boat':
            print(boatmap)
###
        else:
            # Boat was not hit so we find the best option out of remaining adjacent coords
            continue
        
    return hit_count

##################################################################################################
# Compares the values of adjacent coords to determine most likely spot for boat
def compareValues(hitTarget):

    targets = []
    # For any coords in the inner part of the coords
    if hitTarget[0][0] >= 1 and hitTarget[0][0] <= 8 and hitTarget[0][1] >= 1 and hitTarget[0][1] <= 8:
        targets.append((hitTarget[0][0]+1, hitTarget[0][1]))
        targets.append((hitTarget[0][0], hitTarget[0][1]+1))
        targets.append((hitTarget[0][0]-1, hitTarget[0][1]))
        targets.append((hitTarget[0][0], hitTarget[0][1]-1))

    # Corner of grid
    elif hitTarget[0][0] == 0 and hitTarget[0][1] == 0:
        targets.append((hitTarget[0][0]+1, hitTarget[0][1]))
        targets.append((hitTarget[0][0], hitTarget[0][1]+1))

    elif hitTarget[0][0] == 0 and hitTarget[0][1] == 9:
        targets.append((hitTarget[0][0]+1, hitTarget[0][1]))
        targets.append((hitTarget[0][0], hitTarget[0][1]-1))

    elif hitTarget[0][0] == 9 and hitTarget[0][1] == 0:
        targets.append((hitTarget[0][0]-1, hitTarget[0][1]))
        targets.append((hitTarget[0][0], hitTarget[0][1]+1))

    elif hitTarget[0][0] == 9 and hitTarget[0][1] == 9:
        targets.append((hitTarget[0][0]-1, hitTarget[0][1]))
        targets.append((hitTarget[0][0], hitTarget[0][1]-1))

    # Left colum
    elif hitTarget[0][0] == 0:
        targets.append((hitTarget[0][0]+1, hitTarget[0][1]))
        targets.append((hitTarget[0][0], hitTarget[0][1]+1))
        targets.append((hitTarget[0][0], hitTarget[0][1]))  # Place holder so we can easily figure out the direction we are going in
        targets.append((hitTarget[0][0], hitTarget[0][1]-1))

    # Right colum
    elif hitTarget[0][0] == 9:
        targets.append((hitTarget[0][0]-1, hitTarget[0][1]))
        targets.append((hitTarget[0][0], hitTarget[0][1]-1))
        targets.append((hitTarget[0][0], hitTarget[0][1]))  # Place holder
        targets.append((hitTarget[0][0], hitTarget[0][1]+1))

    # Top row
    elif hitTarget[0][1] == 0:
        targets.append((hitTarget[0][0]+1, hitTarget[0][1]))
        targets.append((hitTarget[0][0], hitTarget[0][1]+1))
        targets.append((hitTarget[0][0]-1, hitTarget[0][1]))
        targets.append((hitTarget[0][0], hitTarget[0][1]))  # Just a placehold so the direction thing lines up

    # Bottom row
    elif hitTarget[0][1] == 9:
        targets.append((hitTarget[0][0]+1, hitTarget[0][1]))
        targets.append((hitTarget[0][0], hitTarget[0][1]-1))
        targets.append((hitTarget[0][0]-1, hitTarget[0][1]))
        targets.append((hitTarget[0][0], hitTarget[0][1]))   # Just a placehold so the direction thing lines up

    maxValue = 0
    direction = 0   # Used to tell if we are moving in the x or y direction
    bestCoord = hitTarget
    iValue = 0  # This will be used to make the max value location be labeled True on the trackingGrid

    for i in range(len(targets)):
        # First check if we have visited the coord before
        if trackingGrid[targets[i][0]][targets[i][1]] == False:
            if boatmap[targets[i][0]][targets[i][1]] > maxValue: # Checking that its the highest value
                maxValue = boatmap[targets[i][0]][targets[i][1]]
                bestCoord = targets[i]
                iValue = i
                if i%2 == 0:
                    direction = 1   # 1 means we are in the x direction
                else:
                    direction = 0   # 0 means y direction

    trackingGrid[targets[iValue][0]][targets[iValue][1]] = True 
    return bestCoord, direction

##################################################################################################
# Finds largest number in the boatmap grid (Most likely spot for a boat to be)
def largestNumber():
    max_num = boatmap[0][0]
    row_index = 0
    col_index = 0

    for i, row in enumerate(boatmap):   # enumerate helps us find the largest value 
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
    # First checks to see if the boat could be in that zone, if we have already checked a coord where the boat could be 
    # we won't bother adding the values to the probability map for the boats
    while z < boat_length:
        if trackingGrid[i][j+z] == True:
            return
        z += 1
    z = 0
    while z < boat_length:
        boatmap[i][j+z] += 1
        z+=1
    
def function_v(i, j, boat_length):
    z = 0
    while z < boat_length:
        if trackingGrid[i+z][j] == True:
            return
        z += 1
    z = 0
    while z < boat_length:
        boatmap[i+z][j] += 1
        z+=1

# Create a probabilty map for where the most likely spot a boat could be
def probMap():
    global boatmap  # Lets us reset the grid everytime we use this function
    boatmap = []
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
                # This line is used for recalculations
                if trackingGrid[i][j] == False: # Will check to see if we have already checked the coord

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
    # This could be made better I think, since i & j are not used
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            row.append(False)

        trackingGrid.append(row)

##################################################################################################
def battleship_ascii_art():
    ascii_art = [
    " ______  ______  ______  ______  __      ______  ______  __  __  __  ______  ",
    "/\  == \/\  __ \/\__  _\/\__  _\/\ \    /\  ___\/\  ___\/\ \_\ \/\ \/\  == \ ",
    "\ \  __<\ \  __ \/_/\ \/\/_/\ \/\ \ \___\ \  __\\ \___  \ \  __ \ \ \ \  _-/ ",
     " \ \_____\ \_\ \_\ \ \_\   \ \_\ \ \_____\ \_____\/\_____\ \_\ \_\ \_\ \_\   ",
      "  \/_____/\/_/\/_/  \/_/    \/_/  \/_____/\/_____/\/_____/\/_/\/_/\/_/\/_/   ",
      "________________________________________________________________________________",
      "________________________________________________________________________________"
    ] 

    for line in ascii_art:
        print(line)
        
    print('STARTING...')
    print()

battleship_ascii_art()
main()
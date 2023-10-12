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

grid_size = 10
hitTarget = [] # This will record grid positions for where we have hit a target

def main():
    if len(hitTarget) != 0:
        # If the list isn't empty it means last shot we hit a boat and need to search for it
        # Check up, down, left right 
        print()
    else:
        print(2,1)
        # Find highest probability and say it
    
# Create a probabilty map for each boat
def probMap():
    boatmap = []
    boat_length = 5
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            row.append(0)

        boatmap.append(row)

    for i in range(grid_size):      # Not adding 1 each time just making the value = 1
        row = []
        for j in range(grid_size):
            if i+boat_length <= grid_size:
                boatmap[i][j]+=1
            elif j+boat_length <= grid_size:
                boatmap[i][j] +=1
            else:
                continue
    print(boatmap)


def grid_creation(grid_size):
    grid = []
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            row.append(False)

        grid.append(row)

probMap()
main()


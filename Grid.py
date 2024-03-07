import random


def getfactors(f):
    factor_x = random.randrange(f*-1,f+1)
    if factor_x==0:
        tmp = random.randrange(0,2)
        if tmp == 0:
             factor_y = -1
        else:
            factor_y = 1
    else:
        factor_y = random.randrange(f*-1,f+1)

    if factor_y !=0:
        factor_y =factor_y//abs(factor_y)
    if factor_x !=0:
        factor_x =factor_x//abs(factor_x)
    
    return factor_x,factor_y

def check_overlap(room_size, room_positions, new_size, new_position, overlap_range=0):
    # Iterate through the list of existing rooms along with their indexes
    for idx, (size, position) in enumerate(zip(room_size, room_positions)):
        if are_rooms_overlapping(position, size, new_position, new_size, overlap_range):
            return idx  # Return the index of the overlapping room
    return -1

def setpos(room, rooms, list_pos, minvalue,maxvalue,factor,roomsize,overlap_range,overlap_factor):
    
    fx,fy=getfactors(factor)
    print(fx)
    
    original_posx = list_pos[0][0]
    original_posy= list_pos[0][1]

    if fx==-1 :
        maxx = original_posx-minvalue
        minx = maxx-maxvalue-roomsize
    else :
        minx = (minvalue+original_posx+roomsize)*fx
        maxx = (minx+maxvalue)*fx

    if fy==-1 :
        maxy = original_posy-minvalue
        miny = maxy-maxvalue-roomsize
    else:
        miny = (minvalue+original_posy+roomsize)*fy
        maxy = (miny+maxvalue)*fy

    if minx==maxx==0 and miny==maxy==0:
        x,y = 0,0
    elif minx==maxx==0:
        x,y = 0,random.randrange(miny,maxy)
    elif miny==maxy==0:
        x,y = random.randrange(minx,maxx),0
    else :
        x,y =random.randrange(minx,maxx),random.randrange(miny,maxy)
    
 
    while check_overlap(rooms,list_pos,room,(x,y),overlap_range)!=-1:
        while are_rooms_overlapping(list_pos[check_overlap(rooms,list_pos,room,(x,y),overlap_range)],rooms[check_overlap(rooms,list_pos,room,(x,y),overlap_range)], (x,y), room,overlap_range):
            fx,fy=getfactors(factor)
            addition=random.randrange(1,overlap_factor)
            if x!=0 and y!=0:
                tmp = random.randrange(0,3)                
                if tmp == 0:
                    x += fx*addition
                elif tmp == 1:
                    y += fy*addition
                else:
                    x += fx*addition
                    y += fy*addition
            elif x==0:
                tmp = random.randrange(0,3)                
                if tmp == 0:
                    x += fx*addition
                elif tmp == 1:
                    y += fy*addition
                else:
                    x += fx*addition
                    y += fy*addition
            else:
                tmp = random.randrange(0,3)                
                if tmp == 0:
                    x += fx*addition
                elif tmp == 1:
                    y += fy*addition
                else:
                    x += fx*addition
                    y += fy*addition
    return x,y

def generatepos(roomlist,overlap_range,min_space,max_space,factor,overlap_factor):
    list_pos=[]
    for i,value in enumerate(roomlist):
        if len(list_pos)==0:
            x,y=0,0
        else:
            x,y= setpos(value, rooms, list_pos,min_space,max_space,factor,roomlist[i-1],overlap_range, overlap_factor)
        list_pos.append((x,y))
    return list_pos

def get_room_positions(room_pos, room_size):
    room_positions = []
    minx, miny = room_pos
    maxx = minx + room_size
    maxy = miny + room_size
    
    for x in range(minx, maxx):
        for y in range(miny, maxy):
            room_positions.append((x, y))
    
    return room_positions

def are_rooms_overlapping(pos1, size1, pos2, size2, overlap_range):
    # Extract position components
    x1, y1 = pos1
    x2, y2 = pos2
    
     # Calculate boundaries of each room
    room1_left = x1 - overlap_range
    room1_right = x1 + size1 + overlap_range
    room1_top = y1 - overlap_range
    room1_bottom = y1 + size1 + overlap_range
    
    room2_left = x2
    room2_right = x2 + size2
    room2_top = y2
    room2_bottom = y2 + size2
    
    # Check for overlap
    if (room1_left < room2_right and
        room1_right > room2_left and
        room1_top < room2_bottom and
        room1_bottom > room2_top):
        return True
    else:
        return False


def display_2D(lst, height, width,):
    if height * width != len(lst):
        print("Error: Height times width must be equal to the length of the list.")
        return
    
    for i in range(height):
        for j in range(width):
            print(lst[i * width + j], end=" ")
        print()

def set_entrance(room_size):
    tmpX=random.randrange(0,2)
    tmpY=random.randrange(0,2)
    if tmpX==0:
        x=random.randrange(0,room_size)
    else:
        x=0

    if tmpY==0:
        y=random.randrange(0,room_size)
    else:
        y=0

    return x,y

def generate_grid(rooms,overlap_range, min_space,max_space,factor, overlap_factor, border_range):

    list_pos = generatepos(rooms,overlap_range, min_space, max_space,factor, overlap_factor)
    
    # Random adjustments for top, bottom, left, and right rows and columns
    top_rows = random.randrange(0,border_range)
    bottom_rows = random.randrange(0,border_range)
    left_columns = random.randrange(0,border_range)
    right_columns = random.randrange(0,border_range)
    print("Top rows :"+str(top_rows))
    print("Bottom rows :"+str(bottom_rows))
    print("Left columns :"+str(left_columns))
    print("Right columns :"+str(right_columns))

    print(list_pos)
    list_pos = [(x + left_columns, y + top_rows) for x, y in list_pos]

    

    max_x = max(x + room_size for (x, _), room_size in zip(list_pos, rooms))
    max_y = max(y + room_size for (_, y), room_size in zip(list_pos, rooms))
    min_x = min(x for x, _ in list_pos)
    min_y = min(y for _, y in list_pos)
    list_pos = [(x + left_columns, y + top_rows) for x, y in list_pos]
    print(rooms)
    print(list_pos)

    grid_width = (max_x - min_x) + left_columns + right_columns
    grid_height = (max_y - min_y) + top_rows + bottom_rows
    
    grid = ["."] * (grid_width * grid_height)

    for i, (x, y) in enumerate(list_pos):
        room_index = i
        room_size = rooms[room_index]
        entranceX, entranceY = set_entrance(room_size)
        for j in range(y, y + room_size):
            for k in range(x, x + room_size):
                if j==y+entranceY and k==x+entranceX:
                    grid[(j - min_y) * grid_width + (k - min_x)] = "E" #str(room_index)
                else:    
                    grid[(j - min_y) * grid_width + (k - min_x)] = "X" #str(room_index)

    display_2D(grid, grid_height, grid_width)

    print(grid_width)
    print(grid_height)
    

if __name__ == "__main__":
    nb=int(input("Enter the number of rooms :"))
    max_room_size=int(input("Enter max size :"))
    rooms=[]
    for i in range(nb):
        rooms.append(random.randrange(2,max_room_size+1))
    generate_grid(rooms,overlap_range=4,min_space=2,max_space=10,factor=2,overlap_factor=3,border_range=10)



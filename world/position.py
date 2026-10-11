from os import system
block_place={}
center_x=25
center_y=5
def refresh():
    system("clear")
    for row in range(10):    
        for col in range(50):
            if (col,row) in block_place:
                print("█",end="")
            else:
                print(" ",end="")
        print()
def create_block(x,y):
    real_x=center_x-x
    real_y=center_y-y
    if (real_x,real_y) in block_place:
        print("Error!")
    block_place[(real_x,real_y)]=True
    refresh()
def delete_block(x,y):
    real_x=center_x-x
    real_y=center_y-y
    if (real_x,real_y) not in block_place:
        print("Error!")
    del block_place[(real_x,real_y)]
    refresh()
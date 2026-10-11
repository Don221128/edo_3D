block_place={}
def initialization():
    for _ in range(50):
        print("█",end="")
    print()
def create_block(x,y,z):
    if (x,y,z) in block_place:
        print("Error!")
    block_place[(x,y,z)]=True
    print(block_place)
def delete_block(x,y,z):
    if (x,y,z) not in block_place:
        print("Error!")
    del block_place[(x,y,z)]
    print(block_place)
import position
from time import sleep
index=-50
for _ in range(100):
    index+=1
    position.create_block(index,0)
sleep(5)
index=-50
for _ in range(100):
    index+=1
    position.delete_block(index,0)
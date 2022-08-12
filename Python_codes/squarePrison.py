import random
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
mc = Minecraft.create()
a=True
while (a!=False):
    sleep(60)
    cube= random.uniform(1,95)
    pos = mc.player.getTilePos()
    posFinal = list(filter(lambda x: type(x)==int, pos))
    print(posFinal)
    mc.setBlocks(posFinal[0]+5,posFinal[1]-1,posFinal[2]+5,posFinal[0]-5,posFinal[1]+8,posFinal[2]-5,cube)
    mc.setBlocks(posFinal[0]+4,posFinal[1],posFinal[2]+4,posFinal[0]-4,posFinal[1]+7,posFinal[2]-4,block.AIR.id)
    

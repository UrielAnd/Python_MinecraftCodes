from mcpi.minecraft  import Minecraft
from mcpi import block
from math import *
import time

def walk(posFinal):
     air = mc.getBlock(posFinal[0],posFinal[1]-1,posFinal[2])
     if air!=0:
         mc.setBlocks(posFinal[0]-rang,posFinal[1]-1,posFinal[2]-rang,posFinal[0]+rang,posFinal[1]-1,posFinal[2]+rang, block)#x and z -coordinate
mc = Minecraft.create()
block = 161  #enter the block id you want from minecraft
rang = 3   #enter the distance of the range of the blocks
a = True
while(a==True):
     pos = mc.player.getTilePos()
     print (pos)    #info
     posFinal=list(filter(lambda x: type(x)==int, pos)) #filter to transform Vec3 into vector
     print (posFinal[0],posFinal[1],posFinal[2])  #info
     walk(posFinal)     #call the function

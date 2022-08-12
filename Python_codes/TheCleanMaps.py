from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
mc = Minecraft.create()
pos = mc.player.getTilePos()
rang = 0    #auxiliary variables
a = 0     #auxiliary variables
print (pos)    #info
posFinal=list(filter(lambda x: type(x)==int, pos)) #filter to transform Vec3 into vector
print (posFinal[0],posFinal[1],posFinal[2])  #info
while (a<=100):
    mc.setBlocks(posFinal[0]+1+rang,posFinal[1],posFinal[2]-12,posFinal[0]+1+rang,posFinal[1]-12,posFinal[2]+12, block.AIR.id)      #Spawn Block x,y,z-coordinate
    sleep(0.2)
    mc.setBlocks(posFinal[0]+1+rang,posFinal[1]-8,posFinal[2]-12,posFinal[0]+1+rang,posFinal[1]+12,posFinal[2]+12, block.STONE.id)      #Spawn Block x,y,z-coordinate
    sleep(0.2)
    mc.setBlocks(posFinal[0]+1+rang,posFinal[1]-8,posFinal[2]-12,posFinal[0]+1+rang,posFinal[1]+12,posFinal[2]+12, block.AIR.id)        #Spawn Block x,y,z-coordinate
    rang=rang+1     #auxiliary variables
    a=a+1   #auxiliary variables
    




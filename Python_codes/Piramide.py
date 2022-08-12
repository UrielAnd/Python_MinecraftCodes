from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
mc = Minecraft.create()
pos = mc.player.getTilePos()
repet = 15
#print(pos)
posFinal = list(filter(lambda x: type(x)==int, pos))
print(posFinal)
aux = 0
while (repet > 0):
    mc.setBlocks(posFinal[0]-repet,posFinal[1]+aux,posFinal[2]-repet,posFinal[0]+repet,posFinal[1]+aux,posFinal[2]+repet, block.SANDSTONE.id)
    if (repet!=1):
        mc.setBlocks(posFinal[0]-repet+1,posFinal[1]+aux,posFinal[2]-repet+1,posFinal[0]+repet-1,posFinal[1]+aux,posFinal[2]+repet-1, block.AIR.id)
    repet = repet - 1
    aux = aux + 1
    sleep(0.8)

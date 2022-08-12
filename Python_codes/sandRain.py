import random
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
mc = Minecraft.create()
a=True
while (a!=False):
    pos = mc.player.getTilePos()
    posFinal = list(filter(lambda x: type(x)==int, pos))
    print(posFinal)
    sleep(0.1)
    posRand1 = random.randint(posFinal[0],posFinal[0]+60)
    aux = posFinal[2] -60
    posRand2 = random.randint(aux,posFinal[2])
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    sleep(0.1)
    ########################
    posRand2 = random.randint(posFinal[2],posFinal[2]+60)
    mc.setBlock(posRand1,posFinal[1]+50,posFinal[2],block.SAND.id)
    mc.setBlock(posFinal[0],posFinal[1]+50,posRand2,block.SAND.id)
    ########################
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    sleep(0.1)
    ########################
    aux = posFinal[0] -60
    posRand1 = random.randint(aux,posFinal[0])
    mc.setBlock(posRand1,posFinal[1]+20,posFinal[2],block.SAND.id)
    sleep(0.1)
    ########################
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    sleep(0.1)
    ########################
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    sleep(0.1)
    ########################
    aux = posFinal[2] -60
    posRand2 = random.randint(aux,posFinal[2])
    mc.setBlock(posFinal[0],posFinal[1]+50,posRand2,block.SAND.id)
    sleep(0.1)
    ########################
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)
    mc.setBlock(posRand1,posFinal[1]+50,posRand2,block.SAND.id)


from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
mc = Minecraft.create()
pos = mc.player.getTilePos()
repet = 1
#print(pos)
posFinal = list(filter(lambda x: type(x)==int, pos))
print(posFinal)
aux = 1
while(repet <= 10):
  mc.setBlocks(posFinal[0]-repet,posFinal[1]+repet,posFinal[2]-repet,posFinal[0]+repet,posFinal[1]+repet,posFinal[2]+repet, 95,2)
  if(repet==10):
    sleep(0.5)
    mc.setBlocks(posFinal[0]-repet,posFinal[1]+repet+1,posFinal[2]-repet,posFinal[0]+repet,posFinal[1]+repet+1,posFinal[2]+repet, 95,2)
  if(repet==10):
    while(aux<10):
      sleep(0.5)
      mc.setBlocks(posFinal[0]-repet+aux,posFinal[1]+repet+aux+1,posFinal[2]-repet+aux,posFinal[0]+repet-aux,posFinal[1]+repet+aux+1,posFinal[2]+repet-aux, 95,2)
      aux=aux+1
  repet=repet+1
  sleep(0.5)

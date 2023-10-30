from ctypes import *


class Place:
    name:str
    cost:int
    roadCost:int
    salePrice:int
    placeType:int
    firstearning:int
    def __init__(self, name,firstEarning,cost,roadCost,placeType):
        self.name = name
        self.firstearning = firstEarning
        self.cost = cost
        self.roadCost = roadCost
        self.placeType = placeType

place = [None]*64
place[0]=Place("Arbington", 0, 0, 0, 0)
place[16]=Place("Bredwardine", 0, 0, 0, 2)
place[32]=Place("Dangarnon", 0, 0, 0, 2)
place[48]=Place("Hwen", 0, 0, 0, 2)
place[11]=Place("Fallkirk", 0, 0, 0, 2)
place[19]=Place("Coombe", 0, 0, 0, 2)
place[26]=Place("Kameeraska", 0, 0, 0, 2)
place[37]=Place("Blackburn", 0, 0, 0, 2)
place[56]=Place("Farnfoss", 0, 0, 0, 2)
place[3]=Place("Tylwaerdreath", 0, 0, 0, 3)
place[22]=Place("Lhanbryde", 0, 0, 0, 3)
place[40]=Place("Holmfirth", 0, 0, 0, 3)
place[51]=Place("Blaenau", 0, 0, 0, 3)
place[1]=Place("Emelle", 4096, 8704, 1536, 1)
place[2]=Place("Bracklewhyte", 0x2000, 16640, 2304, 1)
place[4]=Place("Aethelney", 0x2000, 16896, 2048, 1)
place[5]=Place("Warthford", 12288, 22272, 5120, 1)
place[6]=Place("Tywardreath", 0x2000, 14592, 2304, 1)
place[7]=Place("Frostford", 12288, 22528, 5376, 1)
place[8]=Place("Stanmore", 0x4000, 28672, 6400, 1)
place[9]=Place("Caerleon", 0x2000, 0x4000, 2304, 1)
place[10]=Place("Wimborne", 12288, 22272, 5120, 1)
place[12]=Place("Arkaley", 0x2000, 16896, 2128, 1)
place[13]=Place("Stamford", 0x4000, 28928, 6400, 1)
place[14]=Place("Lanercoast", 0x4000, 29184, 0x2000, 1)
place[15]=Place("Erast", 0x2000, 16640, 2048, 1)
place[17]=Place("Airedale", 12288, 22272, 5120, 1)
place[18]=Place("Wallowdale", 0x2000, 16640, 2304, 1)
place[19]=Place("Limesvilles", 12288, 22272, 4864, 1)
place[20]=Place("Greenflower", 0x2000, 16896, 2048, 1)
place[21]=Place("Landow", 4096, 8704, 1536, 1)
place[23]=Place("Falkirk", 4096, 8960, 1536, 1)
place[24]=Place("Rotherham", 4096, 8704, 1536, 1)
place[25]=Place("Windrip", 12288, 22528, 4864, 1)
place[27]=Place("Ilragorn", 0x2000, 16640, 2304, 1)
place[28]=Place("Worcester", 0x4000, 28928, 6400, 1)
place[29]=Place("Drumnacanvy", 4096, 8704, 1536, 1)
place[30]=Place("Mirefield", 4096, 8448, 1536, 1)
place[31]=Place("Langdale", 24576, 45056, 12288, 1)
place[33]=Place("Hadleigh", 12288, 22016, 5376, 1)
place[34]=Place("Astrakane", 4096, 8704, 1536, 1)
place[35]=Place("Aempleforth", 24576, 45056, 12800, 1)
place[36]=Place("Braedwardith", 12288, 22016, 5120, 1)
place[37]=Place("Lerwick", 4096, 0x2000, 1536, 1)
place[38]=Place("Rutherglen", 4096, 0x2000, 1536, 1)
place[39]=Place("Northpass", 20480, 35072, 11520, 1)
place[41]=Place("Sarton", 20480, 35328, 11264, 1)
place[42]=Place("Helmfirth", 0x2000, 16896, 2048, 1)
place[43]=Place("Moressley", 20480, 35072, 11520, 1)
place[44]=Place("Halivaara", 0x4000, 29440, 6912, 1)
place[45]=Place("Burnsley", 0x2000, 0x4000, 2048, 1)
place[46]=Place("Farncombe", 4096, 8704, 1536, 1)
place[47]=Place("Berxley", 20480, 35072, 11264, 1)
place[49]=Place("Timeston", 4096, 8448, 1536, 1)
place[50]=Place("Eastcliff", 20480, 35840, 11520, 1)
place[52]=Place("Claethorpes", 12288, 22272, 5120, 1)
place[53]=Place("Penzance", 20480, 35328, 11520, 1)
place[54]=Place("Dalmellington", 20480, 35072, 11520, 1)
place[55]=Place("Ramshorn", 4096, 8704, 1536, 1)
place[57]=Place("Barnemouth", 20480, 35072, 11264, 1)
place[58]=Place("Sherfield", 4096, 8704, 1536, 1)
place[59]=Place("Lakeshore", 12288, 22528, 5120, 1)
place[60]=Place("Tottenham", 4096, 8448, 1536, 1)
place[61]=Place("Easthaven", 4096, 8960, 1536, 1)
place[62]=Place("Nancledra", 12288, 22016, 5632, 1)
place[63]=Place("Deathfall", 0x4000, 28672, 6400, 1)

libc_path = "attachment/libc-2.27.so"
libc = cdll.LoadLibrary(libc_path)

MAX_place = 0

START = 0
BOUND = 1000000
DEBUG = 0

max_event0 = 0
max_event1 = 0

for seed in range(START, BOUND): # choose seed
  my_location = 0
  ai_location = 0 

  my_action = []
  ai_action = [] 

  my_place = []
  ai_place = []

  tmp_event0 = 0
  tmp_event1 = 0

  libc.srand(seed)

  for i in range(200): # every round N steps

    # my round
    my_location = (my_location+((libc.rand()&0xff) % 0xC) + 1)&0x3f

    if place[my_location].placeType == 2:
      my_action.append(2)

    elif place[my_location].placeType == 3:
      my_event = libc.rand()&0xff
      if my_event > 0xef:
        my_action.append(1)
        tmp_event1 += 1
        if tmp_event1 > max_event1:
          max_event1 = tmp_event1
          print("user double:", max_event1, seed)
      elif my_event < 9:
        my_action.append(0)
      else:
        pass

    else:
      if my_location not in ai_place:
        if my_location not in my_place:
          my_place.append(my_location)
      else:
        my_action.append(2)

    ai_location = (ai_location+((libc.rand()&0xff) % 0xC) + 1)&0x3f
    
    #print(my_location, ai_location)

    if place[ai_location].placeType == 2:
      ai_action.append(2)

    elif place[ai_location].placeType == 3:
      ai_event = libc.rand()&0xff  
      if ai_event > 0xef:
        ai_action.append(1)
      elif ai_event <= 9:
        ai_action.append(0)
        tmp_event0 += 1
        if tmp_event0 > max_event0:
          max_event0 = tmp_event0
          print("ai lose:", max_event0, seed)
      else:
         pass

    else:
      if ai_location not in my_place:
        if ai_location not in ai_place:
          ai_place.append(ai_location)
      else:
        ai_action.append(2)

  if DEBUG:
    print("seed "+str(seed)+"="*0x40)
    print(my_action)
    print(ai_action)
    print(my_place)
    print(ai_place)
    break

print(max_event0)
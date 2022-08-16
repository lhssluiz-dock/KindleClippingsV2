from Services.cleanPositionLine import *

def getPosition(arrayLines, linePosition):
  print(linePosition)
  getPosition = arrayLines[linePosition+1]
  print(getPosition)
  if "Sua nota" in arrayLines[linePosition+1]:
      position = cleanPositionLine(getPosition)
      return position
  else:
    position = cleanPositionLine(getPosition)
    return position
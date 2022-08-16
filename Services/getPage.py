from Services.cleanPageLine import *

def getPage(arrayLines, linePage):
  print(linePage)
  lineWithPosition = arrayLines[linePage+1]
  print(lineWithPosition)
  if "Sua nota" in arrayLines[linePage+1]:
      dirtyPageNumber = lineWithPosition[21:25]
      page = cleanPageLine(dirtyPageNumber)
  else:
      dirtyPageNumber = lineWithPosition[25:30]
      page = cleanPageLine(dirtyPageNumber)
  return page
from operator import concat

def cleanPageLine(dirtyPageNumber):
  page = ""
  for characters in dirtyPageNumber:
    if characters.isdigit():
      page = concat(page,characters)
    else:
      break
  return page
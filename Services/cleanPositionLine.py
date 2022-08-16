from operator import concat

def cleanPositionLine(getPosition):
  position = ""
  if "Sua nota" in getPosition:
    for characters in getPosition[22:27]:
      if characters.isdigit():
        position = concat(position,characters)
      else:
        break
    return position

  if "destaque" in getPosition:
      for characters in getPosition[26:32]:
        if characters.isdigit():
          position = concat(position,characters)
        else:
          break
      return position
import operator
from operator import concat

def ordernateNotesNHighlights(position, notes):
    #tempDict = {position:notes} # Comentei para testar a inversão das notas como chaves e posições como valores
    tempDict = {notes:int(position)}
    dictPositionNotes = dict(sorted(tempDict.items(), key=operator.itemgetter(1)))
    return dictPositionNotes

def ifIsNote(lineInformations, lineContent):
  if "Sua nota" in lineInformations:
    newLineContent = concat("== Nota Pessoal abaixo, do próximo destaque: ", lineContent)
    return newLineContent
  else:
    return lineContent

def markRepeatedNotes(dicionario):
  for chaves, valores in dicionario.items():
      for keys, values in dicionario.items():
          if chaves != keys and valores == values:
              if chaves < keys:
                  dicionario[chaves] = "apagar"
              else:
                  dicionario[keys] = "apagar"
  return dicionario
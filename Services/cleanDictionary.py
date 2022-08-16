lastDict = {}

def cleanDictionary(dicionario):
  for chaves, valores in dicionario.items():
      if valores != "apagar":
          lastDict[chaves] = valores
  return lastDict
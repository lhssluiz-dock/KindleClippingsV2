def openFile(file_path):
    with open(file_path, encoding='utf8') as clippingsFileObject:
        arrayLines = clippingsFileObject.readlines()
    return arrayLines
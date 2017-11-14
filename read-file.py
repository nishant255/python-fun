def readFile(filename):
    with open(filename) as f:
        content = f.readlines()  # read lines from each file
    content = [x.strip() for x in content]  # remove \n from each line
    return content

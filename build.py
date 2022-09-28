import os

components = {}

# build htmlx files


sourceFiles = os.listdir("./src")
componentFiles = os.listdir("./components")

def parseComponents():
    global components
    for componentFile in componentFiles:
        f = open("./components/" + componentFile, "r")

        components[os.path.basename(componentFile)] = f.read()

        f.close()

def formatFile(path):
    
    f = open("./src/" + path, "r")
    output = open(os.path.basename(path).split(".")[0] + ".html", "w")
    print("Output Path: " + os.path.basename(path).split(".")[0] + ".html")


    fileContents = f.read()
    replacedContents = fileContents
    for name in components:
        replacedContents = replacedContents.replace("<" + name.split(".")[0] + " />", components[name])
    output.write(replacedContents)
    output.close()
    f.close()

def formatFiles():
    for file in sourceFiles:
        print("Formatting file " + file + "...")
        formatFile(file)


def main():
    parseComponents()
    formatFiles()

main()
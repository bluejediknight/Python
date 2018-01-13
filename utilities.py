from datetime import datetime
import os
import zipfile
import codecs

def getyyyymmdd():
    now = datetime.now()
    return now.strftime("%Y-%m-%d")   # str(now.year) + str(now.month) + str(now.day)

def writetofile(contents, file):
    f = open(file, "w")
    f.write(contents)
    f.close()

def readcontents(file):
    f = open(file, "r")
    contents = f.read()
    f.close()
    return contents

def getprettydate(date):
    return date.strftime("%A %B %d, %Y")

def getDirectoryContents(loc):
    return open(loc, "r")

def clearDirectoryContents(loc):
    dirs = os.listdir(loc)
    for things in dirs:
            temp = os.path.join(loc, things)
            if os.path.isdir(temp):
                for f in os.listdir(temp):
                    os.remove(os.path.join(temp, f))
                os.rmdir(temp)
            else:
                os.remove(temp)
    print("Cleared contents of " + loc)


def writeAndSave(content, filepath):
    tempfile = codecs.open(filepath, "w+", encoding='utf-8')
    tempfile.write(content)
    tempfile.close()

def zipAndSave(folderToArchive, zippath):    

    #make sure it doesnt exist already
    originalzippath = zippath.replace(".zip", "")
    counter = 2
    while(os.path.exists(zippath)):
        zippath = originalzippath + "_" + str(counter) + ".zip"
        counter += 1
        
    archive = zipfile.ZipFile(zippath, 'w')
    for folder, subfolders, files in os.walk(folderToArchive):
        if folder.startswith(folderToArchive + "\Files"):
            continue
        for file in files:
                archive.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), folderToArchive), compress_type = zipfile.ZIP_DEFLATED)
    archive.close()
    print("Archived " + zippath)

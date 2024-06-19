from zipfile import ZipFile
import os
os.chdir('D:\\Conor')

file = "Testing.zip"
with ZipFile(file,'r') as zip:
    zip.printdir()

    print("Extracting the files")
    zip.extractall()

print("Files Extracted Successfully")
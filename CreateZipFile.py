from zipfile import ZipFile
import os
os.chdir('D:\\Conor')

def get_folder_path(directory):
    paths = []
    for root,directories,files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root,filename)
            paths.append(filepath)
    return paths

directory = "Old_Folder"
paths = get_folder_path(directory)

for file in paths:
    with ZipFile("Shreeya.zip",'a') as zip:
        zip.write(file)
print('Successfully Zipped the files')
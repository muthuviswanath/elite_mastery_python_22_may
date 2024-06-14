import os as fs
import time
# # Get the Current Working Directory
# print(fs.getcwd())
# # Changing the Current Working Directory
# fs.chdir(r"C:\Users\Muthu\Desktop\carousel_images")
# print(fs.getcwd())
# # List Directories and Files
# print(fs.listdir())
# # Remove/Delete a directory or file
# fs.rmdir('Recent Trips')
# time.sleep(10)
# # Create Directories
# fs.mkdir('Bakrid Images')
# print(fs.listdir())
# # Rename Directory
# time.sleep(10)
# fs.rename('Bakrid Images','Recent Trips')
# print(fs.listdir())

# Join and split the path
mypath = fs.path.join('D:','Muthu')
print(mypath)
mypaths= fs.path.split('C:Users\\Muthu\\Desktop')
print(mypaths)
# Check if a directory exisits
print(fs.path.exists('C:Users\\Muthu\\Desktop'))
# Recursively Travers a directory
myfav_folder = 'D:\\2024_OIG_SAM'
for roots,dirs,files in fs.walk(myfav_folder):
    print(roots,dirs,files)
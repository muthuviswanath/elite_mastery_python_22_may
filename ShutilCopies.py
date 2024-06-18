import os
import shutil
#copy()
os.chdir('C:\\Users\\Muthu\\Desktop')
shutil.copy('Divya.txt' ,'Aashish.txt')
# #copy2()
shutil.copy2('Aashish.txt', 'Kapil.txt')
# #copyfile()
shutil.copyfile('Kapil.txt', 'Tendulkar.txt')
#copyfileobj()
src_file = open('Tendulkar.txt','rb')
destn_file= open('Dhoni.txt','wb')
shutil.copyfileobj(src_file,destn_file)

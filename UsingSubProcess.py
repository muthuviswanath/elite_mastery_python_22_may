#call()
import os, subprocess
os.chdir('C:\\Users\\Muthu\\Desktop')
status = subprocess.call('copy Muthu.txt Roopa.txt',shell = True)
if status !=0:
    if status <0:
        print(f"Killed by signal {status}")
    else:
        print(f"Copy Command failed with the return code {status}")
else:
    print("Successfully Copied the file")

    
#check_output()
status = subprocess.check_output('copy Roopa.txt Divya.txt',shell = True)

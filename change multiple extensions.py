import os
import platform

print("Welcome to renamer")
print("i notice that you are running",platform.system())


#the path to the files (the folder)
directory = input("please enter the path to the files , or leave it empty if the files exists in the same directory as this file :\n")
#NOTE::lower the extension so that it won't be a problem in comaprision which is also lowered
current_extension = input("enter the current extension: ").lower()
new_extension = input("enter the new extension: ").lower()
#cancel any whitespaces if there is any
directory = directory.strip(" ")
#to count the numbre of files modified
file_counter = 0
#if there's a directory
if len(directory) > 1 :
    #load the files in that directory to files
    files = os.listdir(directory)
    #loop throw files to search for any file with that extension user provided
    for file in files:
        strFile = file
        file = file.split('.')
        #if the file has already an extension
        if len(file) > 1:
            #if the file has extension we look for
            if file[1].lower() in current_extension:
                #print the file name before and after and transfer them to a string concatenated with the path
                print(current_extension, " file founded")
                if(platform.system() in "Linux"):
                    newName = directory + "/" + file[0] + "." + new_extension
                    strFile = directory + "/" + strFile
                else:
                    newName = directory+"\\"+file[0] + "." + new_extension
                    strFile = directory+"\\"+strFile
                print("old name is ", strFile, end=">>")
                print("new name is ", newName)
                #rename it
                os.rename(strFile, newName)
                #on more file has been modified
                file_counter += 1
                print(file_counter, " file renamed")
#if the directory is empty , the same as the first mechanism , except that the path is not concatenated to the file name
else:
    files = os.listdir()
    for file in files:
        strFile = file
        file = file.split('.')
        if len(file) > 1:
            if file[1].lower() is current_extension:
                print(current_extension, " file founded")
                newName = file[0] + "." + new_extension
                print("old name is ", strFile, end=">>")
                print("new name is ", newName)
                os.rename(strFile, newName)
                file_counter += 1
                print(file_counter, " file renamed")

#print the result
print("the directory to look in is :%s\nprev_extension is : %s\nnew_extension is : %s"%(directory,current_extension,new_extension))
print("done\n%d file(s) renamed from .%s to .%s"%(file_counter,current_extension,new_extension))

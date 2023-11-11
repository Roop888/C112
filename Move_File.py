import os
import shutil

from_dir= "c:/Users/Roop/Downloads"
to_dir= "c:/Users/Roop/Desktop/Document_files"

list_of_files= os.listdir(from_dir)
print (list_of_files)

for file in list_of_files:
    name,extension=os.path.splitext(file)
   # print(name,extension)
    if extension=='':
        continue
    if extension in ["txt", ".doc", ".docx", ".pdf"]:
        path1=from_dir+'/'+file
        path2=to_dir
        path3=to_dir+'/'+file
        if os.path.exists(path2):
            print("moving"+file+"....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)

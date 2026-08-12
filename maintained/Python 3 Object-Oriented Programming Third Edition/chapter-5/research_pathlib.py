from pathlib import Path 
from pprint import pprint 

'''Python pathlib provides an object-orirntrd approch to work with 
files and directories'''

# list of function & methodes used from module:
# .iterdir()  ,  .is_dir()  ,  .glob()  ,  .resolve()  ,  .exists() 
# .is_file()  ,  .stat()    ,  .name

#_______________________________________________________________________

# 1. List Subdirectories and Files inside a Directory.

path = Path('P:\\Projects') 


subdirs = [] 
files   = [] 

for x in path.iterdir(): # iterate over files in the path 
    if x.is_dir(): 
        subdirs.append(x) 
    else:
        files.append(x)

# print(subdirs,'\n')
# print(files,'\n')

#_______________________________________________________________________

# 2. Listing specific type of files 

from pathlib import Path 

path = Path("C:\\Chris")  


pdf_files = path.glob('**/*.pdf') 

# for pf in pdf_files:
#     print(pf) 

# *. list all file in dir and subfolders 
# **/*. go back one dir and start listing 

#_______________________________________________________________________

# 3. Resolving Symbolic links to Canonical Path

#   full_path = 'P:\Projects\OOP3\chapter05\zip_folder\cat image.jpg'
relative_path = Path(r'.\zip_folder\cat image.jpg')

print(relative_path)
print(relative_path.resolve())

#_______________________________________________________________________

# 4. Check if a File or Directory Exists 

full_path = Path(r'P:\Projects\OOP3\chapter05\zip_folder\cat image.jpg')

print(full_path.exists())

#_______________________________________________________________________

# 5. Opening and Reading File Contents 

file_path = Path(
    r'P:\Projects\OOP3\chapter05\zip_folder\the red fox.txt'
)

with open(file_path,'r') as _file:
    _file = _file.readline() 
    print(_file)

#_______________________________________________________________________

# 6. Getting Information of the File 

print(file_path.stat())

#_______________________________________________________________________

# 7. Getting the file or directory name. 
# we can use the property to get the file name from the path object.

path1 = Path(r'.\chapter05\zip_folder\the red fox.txt')
path2 = Path(r'.\chapter05\zip_folder')

print(path1.name)
print(path2.name)

#_______________________________________________________________________

# 8. Creating a new directory 

from pathlib import Path
new_path = r'P:\projects\testfolder'
new_path = Path(new_path)
new_path.mkdir()


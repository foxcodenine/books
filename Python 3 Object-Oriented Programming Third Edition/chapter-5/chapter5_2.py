import sys 
import shutil 
import zipfile 
from pathlib import Path

# New function / methods used:
# from pathlib module:  Path.mkdir()     , Path.iterdir(),
# from zipfile:         zipfile.ZipFile(),  .extractall(),
# from shutil :         shutil.rmtree()
# .replace(oldstring, newstring) 

class ZipReplace: 
    def __init__(self, filename, search_string, replace_string):
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = Path(f"unzipped-{filename}")  
    
    def zip_find_replace(self): 
        self.unzip_files() 
        self.find_replace() 
        self.zip_files() 

    def unzip_files(self):
        self.temp_directory.mkdir() 
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(self.temp_directory)

    def find_replace(self):
        for filename in self.temp_directory.iterdir():
            with filename.open() as file: 
                contents = file.read() 
            contents = contents.replace(
                self.search_string, self.replace_string
            )
            with filename.open("w") as file:
                file.write(contents) 
     

    def zip_files(self):
        with zipfile.ZipFile(self.filename, "w") as file: 
            for filename in self.temp_directory.iterdir():
                file.write(filename, filename.name) 
            shutil.rmtree(self.temp_directory) 


colorfile = ZipReplace('sample_zip_file.zip', ' hi chris ', 'hello')



# Try to redo this class onmy own.
class ZipChange:
    """A Clss that open a zipfile, change file contant 
    and rewrite zipfile"""

    def __init__(self, zipfile, string, _replace):
        self.zipfile = zipfile 
        self.string  = string 
        self._replace = _replace 
        self.temp_dir = Path(f"temp_{zipfile}")

    def action(self):
        self.extract_zip() 
        self.change_zip() 
        self.close_zip() 
    
    def extract_zip(self):
        self.temp_dir.mkdir() 
        with zipfile.ZipFile(self.zipfile) as original: 
            original.extractall(self.temp_dir)

    def change_zip(self): 
        for _file in self.temp_dir.iterdir():
            with _file.open() as contents:
                contents = contents.read() 
            contents = contents.replace(
                self.string, self._replace
            )
            with _file.open('w') as new_file: 
                new_file.write(contents) 

    def close_zip(self):
        with zipfile.ZipFile(self.zipfile, 'w') as newzip:
            for _file in self.temp_dir.iterdir():
                newzip.write(_file, _file.name) 
        shutil.rmtree(self.temp_dir)
        


# Testing the classes      
# colorfiletilles = ZipChange('sample_zip_file.zip',' I did it! ', 'hello')

# if __name__ == '__main__':
#     colorfiletilles.action()    

# if __name__ == "__main__": 
#     ZipReplace(*sys.argv[1:4]).zip_find_replace()

# print(*sys.argv)
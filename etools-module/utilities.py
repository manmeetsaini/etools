import sys
import os
import shutil
import etools
from etools import SSH
class Directory(SSH):
    current_path=os.path.dirname(os.path.abspath(__file__))
    path = current_path+r'\temp'
    def __init__():
        pass

    def create():
        temp_dir= Directory.path
        if not os.path.exists(temp_dir):
            try:
                print ("entering fn")
                os.makedirs(temp_dir)
                print ("Temp directory Created at",temp_dir)
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        else:
            print ("Directory already exist!!")
    def delete():
        temp_dir = Directory.path
        if os.path.exists(temp_dir):
            try:
                shutil.rmtree(temp_dir)
                print ("Temp directory Deleted")
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        else:
            print ("Directory doesn't exist")
   
if __name__=="__main__":
    Directory.create()

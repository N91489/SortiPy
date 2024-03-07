import os
import pickle
from pathlib import Path
import shutil
from itertools import zip_longest

current_dir = os.path.dirname(os.path.abspath(__file__))
path_path = os.path.join(current_dir,"SortiPy-Data/path.pickle")
properties_path = os.path.join(current_dir,"SortiPy-Data/folder_propertise.pickle")

class file_sorter:

    #path set & load function
    def path(p = None):

        #return path location
        if (p == None):
            with open(path_path,"rb") as f:
                pc = pickle.load(f)

            if(os.path.exists(pc)):
                return pc
            else:
                pc = -1
                return pc
            
        #set new path with error handling for non existing path
        else:
            if(os.path.exists(p)):
                with open(path_path,"wb") as f:
                    pickle.dump(p,f,pickle.HIGHEST_PROTOCOL)
                return p
            
            else:
                return -1

    #propertise set & load function
    def properties(ch = None,name = None,extensions = None):

        with open(properties_path,"rb") as f:
                properties = pickle.load(f)
        
        #return propertise list
        if(ch == None):
            return properties

        #print properties list transposed    
        elif(ch == 0):
            
            transposed = list(zip_longest(*properties))
            return transposed
        
        #properties add
        elif(ch == 1):
            l = extensions.split(",")
            l.insert(0,name)
            properties.append(l)

        #propertise remove
        elif(ch == 2):
            name_found = False
            for x in range(0,len(properties)):
                if(properties[x][0] == name):
                    del properties[x]
                    name_found = True
                    break

            if (name_found == False):    
                return -1

        #save changes
        with open(properties_path,"wb") as f:
            pickle.dump(properties,f,pickle.HIGHEST_PROTOCOL)

            
    #sort function
    def sort():
        
        #path calling
        path = Path(file_sorter.path())

        #Folders with File Extensions 
        with open(properties_path,"rb") as f:
            properties=pickle.load(f)

        #All Files & Suffixes in Directory
        files =[x.name for x in path.iterdir() if x.is_file()]
        sufx=[x.suffix for x in path.iterdir() if x.is_file()]

        #Folder Creation And Check
        for i in range(0,len(properties)):
            try:
                os.mkdir(os.path.join(path,properties[i][0]))
            except:
                print(properties[i][0]," File Already Exist...Skipping Its Creation")

        for s in range(0,len(sufx)):
            for ir,row in enumerate(properties):
                for elements in row[1:]:
                    if(sufx[s] == elements):
                        shutil.move(os.path.join(path,files[s]),os.path.join(path,properties[ir][0]))
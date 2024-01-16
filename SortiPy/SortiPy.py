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

        if (p == None):
            with open(path_path,"rb") as f:
                return pickle.load(f)
        
        else:
            if(os.path.exists(p)):
                with open(path_path,"wb") as f:
                    pickle.dump(p,f,pickle.HIGHEST_PROTOCOL)
                return p
            
            else:
                print("Path Doesn't Exist")

    #propertise set & load function
    def properties(ch = None):

        with open(properties_path,"rb") as f:
                properties = pickle.load(f)
        
        #return propertise list
        if(ch == None):
            return properties

        #print properties list transposed    
        elif(ch == 0):
            print("Current Folder & Its Extension:\n")
            transposed = list(zip_longest(*properties))
            for sublist in transposed:
                print(sublist)

        #properties add
        elif(ch == 1):
            name = input("Enter Folder Name: ")
            extensions = input("Enter Extensions(seperate with ,): ")
            l = extensions.split(",")
            l.insert(0,name)
            properties.append(l)

        #propertise remove
        elif(ch == 2):
            name = input("Enter Folder Name: ")

            name_found = False
            for x in range(0,len(properties)):

                if(properties[x][0] == name):
                    del properties[x]
                    print(name,"Folder & Its Propertise Are Removed")
                    name_found = True
                    break

            if (name_found == False):    
                print("No Folder Named",name,"Properties Not Changed")

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

class menu:
    def main():
        print("----------------------------------------")
        print("Welcome To File Sorter")
        while True:
            print("----------------------------------------")
            print("1.Sort\n2.Change Path (Current:",file_sorter.path(),")\n3.Change Folder Properties\n4.Exit")
            print("----------------------------------------")
            ch = int(input("Enter Choice: "))
            print("----------------------------------------")

            if(ch == 4):
                break

            elif(ch == 1):
                file_sorter.sort()

            elif(ch == 2):
                x = input("Enter new Path: ")
                file_sorter.path(x)
                print("New Path set as ",file_sorter.path())

            elif(ch == 3):
                file_sorter.properties(0)
                print("----------------------------------------")
                ch2 = int(input("\n1.Add Folder & Its Extension\n2.Remove Folder & Its Extensions\nEnter Choice: "))
                print("----------------------------------------")

                if(ch2 == 1):
                    file_sorter.properties(1)

                elif(ch2 == 2):
                    file_sorter.properties(2)

                else:
                    print("Invalid Choice")
                    
#run               
menu.main()